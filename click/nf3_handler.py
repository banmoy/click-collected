from HandlerTemplate import HandlerTemplate
from utils import get_influx_point


class BitRateHandler(HandlerTemplate):

    def __init__(self):
        self.name = 'nf3.c.bit_rate'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        bitrate = float(data)
        point = get_influx_point(self.name,
                            {'click_time': curtime},
                            {'value': bitrate}
                    )
        return [point]


class BitRateHandler0(HandlerTemplate):

    def __init__(self):
        self.name = 'nf3.c0.bit_rate'

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
        self.name = 'nf3.c1.bit_rate'

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
        self.name = 'nf3.c.rate'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        rate = float(data)
        point = get_influx_point(self.name,
                            {'click_time': curtime},
                            {'value': rate}
                    )
        return [point]


class PktRateHandler0(HandlerTemplate):

    def __init__(self):
        self.name = 'nf3.c0.rate'

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
        self.name = 'nf3.c1.rate'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        rate = float(data)
        point = get_influx_point(self.name,
                            {'click_time': curtime},
                            {'value': rate}
                    )
        return [point]


class TaskThreadHandler(HandlerTemplate):

    def __init__(self):
        self.name = 'nf3.rb.task_thread'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        points = []
        for d in data.split(','):
            t, n = d.split(':')
            point = get_influx_point(
                self.name,
                {
                    'click_time': curtime,
                    'task': t
                },
                {'value': int(n)}
            )
            points.append(point)
        return points


class TaskCostHandler(HandlerTemplate):

    def __init__(self):
        self.name = 'nf3.rb.task_cost'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        points = []
        for d in data.split(','):
            t, n = d.split(':')
            point = get_influx_point(
                self.name,
                {
                    'click_time': curtime,
                    'task': t
                },
                {'value': int(n)}
            )
            points.append(point)
        return points


class TaskCallHandler(HandlerTemplate):

    def __init__(self):
        self.name = 'nf3.rb.task_call'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        points = []
        for d in data.split(','):
            t, n = d.split(':')
            point = get_influx_point(
                self.name,
                {
                    'click_time': curtime,
                    'task': t
                },
                {'value': int(n)}
            )
            points.append(point)
        return points
