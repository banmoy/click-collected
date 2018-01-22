from abc import abstractmethod


class HandlerTemplate:

    def __init__(self):
        pass

    @abstractmethod
    def handler_name(self):
        pass

    @abstractmethod
    def influx_records(self, data, curtime):
        pass
