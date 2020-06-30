# main.py -- put your code here!
import time
import machine
import pycom
from mcp9700 import MCP9700, MCP9700Result

temp_sensor = MCP9700()

while True:
    temp_value = temp_sensor.read_print()
    while not temp_value.input_is_valid():
        time.sleep(1)
        temp_value = temp_sensor.read_print()
    pybytes.send_signal(2, temp_value.degree_celsius)
    temp_sensor.colour_switcher(temp_value.degree_celsius)
    time.sleep(2)
    pycom.heartbeat(False)
    time.sleep(1)
