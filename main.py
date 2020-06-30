# Import the libraries that are recuired
import time
import machine
import pycom
#from mcp9700 import MCP9700, MCP9700Result
import lib.mcp9700

#Create instance of class MCP9700
temp_sensor = MCP9700()

#Reading the temperatur and sending data is placed in a while loop
#since we want to do this repeaditly. First we create a variable which 
#holds the temperature from the sensor. Then there's a inner while loop
#that only executes if the sensor hasn't a valid value, otherwise the outer 
# while loop continues and the data are send to Pybytes, the LED switches color 
#and last the unit wait for 30 seconds until the loop continues. 

while True:
    temp_value = temp_sensor.read_print()
    while not temp_value.input_is_valid():
        time.sleep(1)
        temp_value = temp_sensor.read_print()
    pybytes.send_signal(2, temp_value.degree_celsius)
    temp_sensor.color_switcher(temp_value.degree_celsius)
    time.sleep(2)
    pycom.heartbeat(False)
    time.sleep(30)
