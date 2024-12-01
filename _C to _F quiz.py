#this program will prompt use to input a temp in celsius
#convert that temp to degrees fahrenheit
#ask the user for the temp. in degrees celius
#input always gives us a string of what the user typed
#we can use the float() function to convert a string to a number type instead of text
#float() allows a decimal number input

_C = float(input("Enter a temperature in Celcius: "))

#convert this values to Celsius with python math
_F = (((9/5)* _C) + 32)

#print results
print(_C, "degrees Celcius is", round(_F, 2), "degrees Fahrenheit.")