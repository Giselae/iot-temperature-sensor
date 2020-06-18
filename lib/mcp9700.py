import time
import machine
#import pybytes 

class MCP9700:
    
    def __init__(self):
        adc = machine.ADC()
        self.analogTempPin = adc.channel(pin='P20')

    # def init_adc():
    #     adc = machine.ADC()
        # analogTempPin = adc.channel(pin='P20')
    #     tempValue = analogTempPin()
        
    def read_print(self):
        while True:
            
            milliVolts = self.analogTempPin.voltage()
            degreeCelsius = (milliVolts - 500.0) / 10.0
            print(milliVolts)
            print(degreeCelsius)
            Pybytes.send_signal(2, degreeCelsius)
            time.sleep(1)