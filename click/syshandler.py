from HandlerTemplate import HandlerTemplate
from utils import get_influx_point


class SysRouterNumber(HandlerTemplate):

    def __init__(self):
        self.name = 'sys.cs.router_num'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        num = int(data)
        point = get_influx_point(
                    self.name,
                    {'click_time': curtime},
                    {'value': num}
                )
        return [point]


class SysElementNumber(HandlerTemplate):

    def __init__(self):
        self.name = 'sys.cs.element_num'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        num = int(data)
        point = get_influx_point(
                    self.name,
                    {'click_time': curtime},
                    {'value': num}
                )
        return [point]


class SysThreadNumber(HandlerTemplate):

    def __init__(self):
        self.name = 'sys.cs.thread_num'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        num = int(data)
        point = get_influx_point(
            self.name,
            {'click_time': curtime},
            {'value': num}
        )
        return [point]


class SysElementPerThread(HandlerTemplate):

    def __init__(self):
        self.name = 'sys.cs.element_per_thread'

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
                        'thread': int(t)
                     },
                    {'value': int(n)}
                )
            points.append(point)
        return points


class SysLoadPerThread(HandlerTemplate):

    def __init__(self):
        self.name = 'sys.cs.load_per_thread'

    def handler_name(self):
        return self.name

    def influx_records(self, data, curtime):
        points = []
        for d in data.split(','):
            t, l = d.split(':')
            point = get_influx_point(
                self.name,
                {
                    'click_time': curtime,
                    'thread': t
                },
                {'value': float(l)}
            )
            points.append(point)
        return points
