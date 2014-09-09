#!/usr/bin/python
import sys
import time
import datetime
import requests
import Adafruit_DHT
from time import gmtime, strftime
<<<<<<< HEAD
 
sensor = Adafruit_DHT.DHT22
pin = 4
 
=======

sensor = Adafruit_DHT.DHT22
pin = 4

>>>>>>> 826df4d345590768c93e233f21c61284c5a86c09
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

rest_server="http://192.168.88.252:3000/api/Temperatures"

while True:
  if humidity is not None and temperature is not None:
<<<<<<< HEAD
    ctime=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
=======
    ctime=datetime.datetime.fromtimestamp(time.time(), None)
>>>>>>> 826df4d345590768c93e233f21c61284c5a86c09
    print 'Date={0} Temp={1:0.2f}*C  Humidity={2:0.2f}%'.format(ctime,temperature, humidity)
    payload = {'timestamp': ctime, 'temp': temperature, 'humid': humidity}
    r = requests.post(rest_server, data=payload)
    time.sleep(5)
  else:
    print 'Failed to get reading. Try again!'
