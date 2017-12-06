import time

class ClickClient:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected = False

    def time_tag(self):
        return time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())

    def connect(self):
        pass

    def read_handler_request(self, read_handler):
        return request

    def parse_response(self, response):
        return []

    def response_to_points(self, read_handler, response):
        rep_list = parse_response(response)

    def get(self, request):
        if not self.connected:
            try:
                connect()
                self.connected = True
            except Exception as e:
                pass



    def get_points(self,read_handler):
        request = read_handler_request(read_handler)
        response = get(request)
        return response_to_points(read_handler, response)
