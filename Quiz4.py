#helpful utility functions we can use in other programs
import math

#defin func with constant and paraments
def degrees2radians(x):
    '''
    converting degrees to radians for angles
    :param x: input the angle in degrees
    :return _angleinradians: angle in radians
    '''
    # math computation to convert degree to radian and x is user input
    # one / for decimals
    _angleinradians = (math.pi / 180) * x
#return the value that is now radians to main prog.
    return _angleinradians

# MAIN program
# variable for use input of degrees that can be a float
p = float(input("Enter an angle in degrees: "))
#call function and send user input to defined funct.
v = degrees2radians(p)
#print the inital value and return value to console
print("The angle", p, "degress can be converted to", v, "radians.")
