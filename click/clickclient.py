#!/usr/bin/env python

import socket


class ClickClient:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected = False
        self.buffsize = 4096
        self.data = ''

    def _connect(self):
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sk.connect((self.host, self.port))
        self.sk.recv(self.buffsize)

    def _read_line(self):
        while True:
            index = self.data.find('\n')
            if index >= 0:
                ret = self.data[0:index]
                self.data = self.data[index+1:]
                return ret
            self.data = self.sk.recv(self.buffsize)

    def _read_n(self, size):
        while len(self.data) < size:
            self.data += self.sk.recv(self.buffsize)
        ret = self.data[0:size]
        self.data = self.data[size+1:]
        return ret

    @classmethod
    def _get_response_code(cls, data):
        return data[0:3]

    @classmethod
    def _get_data_size(cls, data):
        i = 0
        while i < len(data) and not data[i].isdigit():
            i += 1
        j = i
        while j < len(data) and data[j].isdigit():
            j += 1
        return int(data[i:j])

    def read(self, handler):
        if not self.connected:
            self._connect()
            self.connected = True
        self.sk.sendall('read ' + handler + '\n')
        line = self._read_line()
        code = self._get_response_code(line)
        if code != '200':
            return None
        line = self._read_line()
        size = self._get_data_size(line)
        data = self._read_n(size)
        return data