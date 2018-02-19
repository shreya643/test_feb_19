'''Q4. Create a Temperature class. Make two methods :
a. convertFahrenheit - It will take Celsius and will print it into Fahrenheit.
b. convertCelsius - It will take Fahrenheit and will convert it into Celsius.'''
class Temperature:

    def convertFahrenheit(c):
        print ("Fahrenheit={}".format(1.8 * c + 32))



    def convertCelsius(f):
        print ("Celsius={}".format((f-32)/1.8))


temp1= Temperature
temp1.convertCelsius(10)
temp1.convertFahrenheit(32)