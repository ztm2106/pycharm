#temp. in fahrenheit and velocity in mph data is stored in two different variables
#variables are transformed by math expressions to determine the windchill in fahrenheit
#Wind chill data is store to be printed later
#float allows for decimal numbers to be stored and printed
_F = float(input("Enter temperature in Fahrenheit: "))
_V = float(input("Enter wind speed in miles per hour: "))

#"**" = Exponentiation
_Wc = (35.74 + 0.6215 * _F + (0.4275 * _F - 35.75) * _V**0.16)

#all variables are print by print()
# print("")adds space between user input data and the printed constants
#round(varible, #) rounds the output to the nearest one decimals places
print("")
print(("The wind chill for"), _F, ("degrees fahrenheit with a wind velocity of"), _V, ("mile per hour is"), round(_Wc, 1), ("degrees Fahrenheit."))