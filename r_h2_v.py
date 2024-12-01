#import util and math modules to use to transform the input user data
import util
import math

height = float(input("Enter units of the radius of a circle: "))
radius = float(input("Enter units of the radius of a circle: "))

volume = util.h2v(height,radius)
print("The volume of a cone with radius", radius, " units and height of", height, "units, the volume of cone is", round(volume, 1), "units cubed.")