# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:30:59 2021

@author: Sr Main
"""

import Adafruit_MAX31855.MAX31855 as MAX31855
import datetime
from influxdb import InfluxDBClient

def collect_temp(temp, measurement_name):
	# Stores values in an array "
    try:
        current_time = str(datetime.datetime.utcnow())
        data_body = [
			{"measurement": "{}".format(measurement_name),
				"time": current_time,
    			"fields": {"channel 1": temp}
				}
			]
        return data_body
    except Exception as e2:
        print("Error storing data:")
        print(e2)

if __name__ == '__main__':
    host = "172.28.82.113"
    port = 8086
    user = "root"
    pwd = "root"
    dbname = "Alexandria"
    CLK1 = 25
    CS1  = 24
    DO1  = 23
    CLK2 = 18
    CS2  = 15
    DO2  = 14
    sensor1 = MAX31855.MAX31855(CLK1, CS1, DO1)
    sensor2 = MAX31855.MAX31855(CLK2, CS2, DO2)    
    tempC1 = sensor1.readTempC()
    tempC2 = sensor2.readTempC()
    temp_data1 = collect_temp(tempC1, "689 heatpipe 1")
    temp_data2 = collect_temp(tempC2, "689 heatpipe 2")
    print("Collected data.")
    client = InfluxDBClient(host, port, user, pwd, dbname)
    client.write_points(temp_data1)
    client.write_points(temp_data2)
    print("Temperature data sent!")
    