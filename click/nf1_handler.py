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
