from HandlerTemplate import HandlerTemplate
from utils import get_influx_point


class BitRateHandler(HandlerTemplate):

    def __init__(self):
        self.name = 'nf1.c.bit_rate'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        bitrate = float(data)
        point = get_influx_point(self.name,
                            {'click_time': curtime},
                            {'value': bitrate}
                    )
        return [point]

class BitRateHandler1(HandlerTemplate):

    def __init__(self):
        self.name = 'nf1.c1.bit_rate'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        bitrate = float(data)
        point = get_influx_point(self.name,
                            {'click_time': curtime},
                            {'value': bitrate}
                    )
        return [point]

class BitRateHandler2(HandlerTemplate):

    def __init__(self):
        self.name = 'nf1.c2.bit_rate'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        bitrate = float(data)
        point = get_influx_point(self.name,
                            {'click_time': curtime},
                            {'value': bitrate}
                    )
        return [point]

class PktRateHandler(HandlerTemplate):

    def __init__(self):
        self.name = 'nf1.c.rate'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        rate = float(data)
        point = get_influx_point(self.name,
                            {'click_time': curtime},
                            {'value': rate}
                    )
        return [point]

class PktRateHandler1(HandlerTemplate):
    def __init__(self):
        self.name = 'nf1.c1.rate'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        rate = float(data)
        point = get_influx_point(self.name,
                                 {'click_time': curtime},
                                 {'value': rate}
                                 )
        return [point]

class PktRateHandler2(HandlerTemplate):
    def __init__(self):
        self.name = 'nf1.c2.rate'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        rate = float(data)
        point = get_influx_point(self.name,
                                 {'click_time': curtime},
                                 {'value': rate}
                                 )
        return [point]