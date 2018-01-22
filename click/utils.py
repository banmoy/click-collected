import time
import inspect
import HandlerTemplate


def time_tag():
    return time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())


def get_influx_point(m, t, f):
    return {
        'measurement': m,
        'tags': t,
        'fields': f
    }


def load_handler(mod_name, handler_names):
    mod = __import__(mod_name)
    handlers = []
    for hn in handler_names:
        hc = getattr(mod, hn)
        handlers.append(hc())
    return handlers