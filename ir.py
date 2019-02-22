'''
Object detection:
below code will make Green led ON when the object is near, else red will remain ON
input will get at pin 14 accordingly we will give output at 3 or 4

information about the functions are at 
https://pythonhosted.org/RPIO/rpio_py.html#gpio-input-output
'''

import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)    # change to BOARD numbering schema

IO.setup(2,IO.OUT)    # GPIO 2 -> Red LED as output
IO.setup(3,IO.OUT)    # GPIO 3 -> Green LED as output
IO.setup(14,IO.IN)    # GPIO 14 -> IR sensor as input

while True:

    if(IO.input(14)==True):     # object is far away
        IO.output(2,True)       # Red led ON
        IO.output(3,False)      # Green led OFF
    
    if(IO.input(14)==False):    # object is near
        IO.output(3,True)       # Green led ON
        IO.output(2,False)      # Red led OFF
