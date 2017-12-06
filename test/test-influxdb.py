
import time
from influxdb import InfluxDBClient


json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "fields": {
            "value": 0.64
        }
    }
]

def main():
    client = InfluxDBClient('localhost', 8086)
    client.create_database('test-influxdb')
    client.switch_database('test-influxdb')
    while True:
        time.sleep(0.05)
        client.write_points(json_body)

if __name__ == '__main__':
    main()
