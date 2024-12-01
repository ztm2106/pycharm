#this program will prompt use to input a temp in fahrenheit
#convert that temp to degrees Celsius
#ask the sure for the temp. in degrees fahrenheit
#input always gives us a string of what the user typed
#we can use the int() or float() function to convert a string to a number type instead of text
#int() always for whole number input and float() allows a decimal number input
_F = float(input("Enter a temperature in Fahrenheit: "))

#convert this values to Celsius
_C = ((5/9)*(_F - 32))

#output the temp. in Celsius
#round(varible, #) rounds the output to the nearest number of decimals specified
print(_F, "degrees Fahrenheit is", round(_C, 1), "degrees Celsius")


