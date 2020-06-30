
import machine
import pycom

class MCP9700Result:

    NO_INPUT = 0
    VALID_INPUT = 1

    error = VALID_INPUT
    degree_celsius = 0

    #Constructor for the class that is created when a temperature is read 
    def __init__(self, error, degree_celsius):
        self.error = error
        self.degree_celsius = degree_celsius

    #Method that confirmes a valid temperature value
    def input_is_valid (self):
        return self.error == MCP9700Result.VALID_INPUT

  
class MCP9700:

    #Constructor that's called in main when a object of MCP9700 is created
    #machine.ADC() is called since the sensor is a analog sensor. 
    def __init__(self):
        adc = machine.ADC()
        self.analogTempPin = adc.channel(pin='P20')
        pycom.heartbeat(False)

    #Method that reads value and print value to the terminal. If the sensor
    #doesn't detect anything a object with error NO_INPUT is returned to main
    #and the inner loop in main continues until the sensor detects a valid value. 
    #If the sensor detects voltage it is converted to celsius, prints the voltage 
    #and the degrees in celsius to the terminal and returns a object with the result 
    #to main. 
    def read_print(self):

        milli_volts = self.analogTempPin.voltage()
        
        if milli_volts == 0:
            return MCP9700Result(self.NO_INPUT, 0)
        else:
            degree_celsius = (milli_volts - 500.0) / 10.0
            print(milli_volts)
            print(degree_celsius)
            return MCP9700Result(MCP9700Result.VALID_INPUT, degree_celsius)
    
    # Method that switches the color of the LED on the Lopy4 depending
    # of the temperature.      
    def color_switcher(self, degree_celsius):
        
        if degree_celsius <=26.0:
            pycom.rgbled(0xe60099)
        elif degree_celsius >=26.1 :
            pycom.rgbled(0x32a8a2)
        elif degree_celsius >=26.8:
            pycom.rgbled(0xa89c32)

    

   
        
       
        
