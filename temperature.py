'''
using senesor dht11 for monitoring a room temperature 
this code will monitor the temperature & humidity at each second
(make sure that the output is connected to pin 15) 

'''

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import dht11 # to connect to the sensor dht11
import time # Import the sleep function from the time module
import datetime # to know time of updated information

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.cleanup() # reset every channel that has been set up by this program 
# and unexport interrupt gpio interfaces

instance = dht11.DHT11(pin=15) # #read the data using pin 15
i=0

while True:  # Run forever
 result = instance.read()   #reading a input from instance into result
 if result.is_valid():      # in case of dht11 failure is_valid() returns false
  print("Last valid input: "+ str(datetime.datetime.now()))
  print("Temperature: %d C" %result.temperature)
  print("Humidity: %d %%" % result.humidity)
 time.sleep(1)
