from influxdb import InfluxDBClient
import datetime
import psutil
import socket
import time

client = InfluxDBClient('localhost', 8086, 'admin', 'admin','test')
client.create_database('test')

def generate_json_body():
    cpu_usage = psutil.cpu_percent()
    hostname = socket.gethostname()
    json_body = [
        {
            "measurement": "cpu_usage",
            "tags": {
                "hostname": hostname
            },
            "time": datetime.datetime.utcnow(),
            "fields": {
                "value": cpu_usage
            }
        }
    ]
    return json_body

while(True):
    client.write_points(generate_json_body())
    time.sleep(1)
    print("adding")