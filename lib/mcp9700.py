import time
import machine
import pycom

class MCP9700Result:

    NO_INPUT = 0
    VALID_INPUT = 1

    error = VALID_INPUT
    degree_celsius = 0

    def __init__(self, error, degree_celsius):
        self.error = error
        self.degree_celsius = degree_celsius

    def input_is_valid (self):
        return self.error == MCP9700Result.VALID_INPUT

  
class MCP9700:

    def __init__(self):
        adc = machine.ADC()
        self.analogTempPin = adc.channel(pin='P20')
        pycom.heartbeat(False)

    def read_print(self):

        milli_volts = self.analogTempPin.voltage()
        
        if milli_volts == 0:
            return MCP9700Result(self.NO_INPUT, 0)
        else:
            degree_celsius = (milli_volts - 500.0) / 10.0
            print(milli_volts)
            print(degree_celsius)
            return MCP9700Result(MCP9700Result.VALID_INPUT, degree_celsius)
         
    def colour_switcher(self, degree_celsius):
        
        if degree_celsius <=26.0:
            pycom.rgbled(0xe60099)
        elif degree_celsius >=26.1 :
            pycom.rgbled(0x32a8a2)
        elif degree_celsius >=26.8:
            pycom.rgbled(0xa89c32)

    

   
        
       
        
