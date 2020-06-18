# main.py -- put your code here!
import time
import machine
from mcp9700 import MCP9700

snurrbo = MCP9700()
snurrbo.read_print()

# adc = machine.ADC()
# analogTempPin = adc.channel(pin='P20')
# tempValue = analogTempPin()

# while True:
    
#     milliVolts = analogTempPin.voltage()
#     degreeCelsius = (milliVolts - 500.0) / 10.0
#     print(milliVolts)
#     print(degreeCelsius)

#     time.sleep(1)