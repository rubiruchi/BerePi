#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, json, math
import socket
import tsdb
import lib.sht25 as sht25
import lib.t110 as t110

def influxdbwrite(obj=None):
	ctx = {}
        dt = (1.0 / 1000) * 1000000  # to microseconds

        ctx['time'] = int(time.time() * 1000000)  # to microseconds
        ctx['id'] = str(1)

	measurement = "%s.%s" % (obj['hostname'], obj['type'])
	metadata = "\
		device= rpi2,\
		sensor= %s,\
		user=   sinbinet\
	" % (obj['type'])
	metadata = metadata.replace(" ", "") 

	tr = tsdb.Transaction(measurement)
	tr.write(value=obj['value'], tag=obj['type'], meta=metadata, timestamp=ctx['time'])
	tr.flush()

def get_CO2(sensor):
	try:
		co2 = sensor.read_co2()
		return co2
	except:
		return False

def readData():
	data = {}
	th = sht25.SHT25()
	cdo = t110.T110()

	while True:
		temp = th.read_temperature()
		humi = th.read_humidity()
		#co2 = cdo.read_co2()

		data['hostname'] = socket.gethostname()
		data['value'] = temp
		data['type'] = 'temp'
		influxdbwrite(data)
		time.sleep(.1)

		data['value'] = humi
		data['type'] = 'humi'
		influxdbwrite(data)
		time.sleep(.1)

		co2 = get_CO2(cdo)
		if co2:
			data['value'] = co2
			data['type'] = 'co2'
			influxdbwrite(data)

		print temp, humi, co2
		time.sleep(10)

if __name__ == "__main__":
	readData()
