import time
from influxdb import InfluxDBClient
from clickclient import ClickClient
from utils import time_tag
from utils import load_handler

# sample interval(s)
INTERVAL = 1

# click
CLICK_HOST = '10.21.5.202'
CLICK_PORT = 12345

# influxdb
INFLUXDB_HOST = '10.21.5.205'
INFLUXDB_PORT = 8086
DATABASE = 'telegraf'

handlers = []


def init():
    influxdb_client = InfluxDBClient(INFLUXDB_HOST, INFLUXDB_PORT)
    influxdb_client.create_database(DATABASE)
    influxdb_client.switch_database(DATABASE)

    click_client = ClickClient(CLICK_HOST, CLICK_PORT)

    global handlers

    handlers += load_handler('syshandler', ['SysRouterNumber', 'SysElementNumber', 'SysThreadNumber', 'SysElementPerThread', 'SysLoadPerThread'])
    handlers += load_handler('nf1_handler', ['BitRateHandler', 'PktRateHandler', 'BitRateHandler1', 'PktRateHandler1', 'BitRateHandler2', 'PktRateHandler2'])
    # handlers += load_handler('nf2_handler', ['BitRateHandler'])
    # handlers += load_handler('nf3_handler', ['TaskThreadHandler', 'TaskCostHandler', 'BitRateHandler', 'BitRateHandler0', 'BitRateHandler1', 'PktRateHandler', 'PktRateHandler0', 'PktRateHandler1'])
    # handlers += load_handler('nf4_handler', ['BitRateHandler'])

    return influxdb_client, click_client


def main():
    influx_client, click_client = init()
    while True:
        curtime = time_tag()
        records = []
        for h in handlers:
            try:
                data = click_client.read(h.handler_name())
                if data is not None and len(data) > 0:
                    records += h.influx_records(data, curtime)
            except Exception as e:
                print h.handler_name() + ": " + str(e)
        try:
            influx_client.write_points(records)
        except Exception as e:
            print 'influx: ' + str(e)
        time.sleep(INTERVAL)


if __name__ == '__main__':
    main()
