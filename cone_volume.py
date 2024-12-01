#radius and height in units data are stored in two different variables with same variable names
#variables are transformed by math expressions to determine the volume of a cone
#the variable Volume stores the math expressions to transforms the radius and height data and is printed later
#float allows for decimal numbers to be stored and printed
radius = float(input("Enter a radius value in units: "))
height = float(input("Enter a height value in units: "))

# the varible pi stores the numerical value of pi to be transformed in the variable volume
pi = 3.14159

#the variable Volume stores the math expressions to transforms the radius, height, and pi value data and is printed later
#"**" = Exponentiation
volume = (pi * (radius**2) * (height/3))






#all variables are print by print()
#print("") adds space between user input data and the printed constants
#round(varible, #) rounds the output to the nearest 3 decimals places
#print is used to tell the computer to print the constants in "" and in the story the user can input data because
#the variable numbered in answers get the values assigned by the input data of the user
print("")
print(("The volume a cone that has a radius of"), radius, ("units and a height of"), height, ("units is"), round(volume, 3), ("cubic units."))