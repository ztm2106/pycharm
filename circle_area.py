#radius in units data are stored in variables with same variable name
#variable are transformed by math expressions to determine the area of a cone
#the variable are stores the math expressions to transforms the radius data and is printed later
#float allows for decimal numbers to be stored and printed
radius = float(input("Enter a radius value in units: "))

# the varible pi stores the numerical value of pi to be transformed in the variable volume
pi = 3.14159

#the variable area stores the math expressions to transforms the radiuscand pi value data and is printed later
#"**" = Exponentiation
area = (pi * (radius**2))

#all variables are print by print()
#print("") adds space between user input data and the printed constants
#round(varible, #) rounds the output to the nearest 3 decimals places
#print is used to tell the computer to print the constants in "" and in the story the user can input data because
#the variable numbered in answers get the values assigned by the input data of the user
print("")
print("The area of a circle with the radius of", radius, "is", round(area, 3), ("in units squared."))