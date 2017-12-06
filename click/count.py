import time
from influxdb import InfluxDBClient
import ClickClient

# sample interval(s)
INTERVAL = 0.05

# click
CLICK_HOST = '10.21.5.202'
CLICK_PORT = 12345
READ_HANDLER = {
    'c' : ['rate', 'bit_rate']
}

# influxdb
INFLUXDB_HOST = '10.21.5.205'
INFLUXDB_PORT = 8086
DATABASE = 'click'


def init():
    influxdb_client = InfluxDBClient(INFLUXDB_HOST, INFLUXDB_PORT)
    influxdb_client.create_database(DATABASE)
    influxdb_client.switch_database(DATABASE)

    click_client = ClickClient(CLICK_HOST, CLICK_PORT)

    return influxdb_client, click_client


def main():
    influx_client, click_client = init()
    count = 0
    while True:
        time.sleep(INTERVAL)
        try:
            points = click_client.get_points(READ_HANDLER)
            influx_client.write_points(points)
            ++count
        except Exception as e:
            print 'failed ' + str(count + 1)


if __name__ == '__main__':
    main()
