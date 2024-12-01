#import util and math modules to use to transform the input user data
import util
import math


radius = float(input("Enter units of the radius of a circle: "))
area = util.c2a(radius)

print("The area of a circle with radius", radius, "units is", round(area, 1), "units squared.")