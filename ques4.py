'''Q4. Create a Temperature class. Make two methods :
a. convertFahrenheit - It will take Celsius and will print it into Fahrenheit.
b. convertCelsius - It will take Fahrenheit and will convert it into Celsius.'''

class Temperature:
    def __init__(self,c,f):
        self.c=c
        self.f=f

    def convertFahrenheit(self):
        print ("Fahrenheit={}".format(1.8 * self.c + 32))


    def convertCelsius(self):
        print ("Celsius={}".format((self.f-32)/1.8))


temp1= Temperature(10,32)
temp1.convertCelsius()
temp1.convertFahrenheit()