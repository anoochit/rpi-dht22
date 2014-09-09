#!/usr/bin/python
import sys
import time
import datetime
import Adafruit_DHT
from time import gmtime, strftime
 
sensor = Adafruit_DHT.DHT22
pin = 4
 
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
 
while True:
  if humidity is not None and temperature is not None:
    #ctime=strftime("%a, %d %b %Y %X +0000", gmtime())
    ctime=datetime.datetime.fromtimestamp(time.time(), None)
    print 'Date={0} Temp={1:0.2f}*C  Humidity={2:0.2f}%'.format(ctime,temperature, humidity)
    time.sleep(5)
  else:
    print 'Failed to get reading. Try again!'
