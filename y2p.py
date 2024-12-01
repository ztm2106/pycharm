#import util and math modules to use to transform the input user data
import util
import math

years = float(input("Enter the amount a number of years from now: "))

newpop= util.y2p(years)
print("From", years, "years, the new population will be about", int(newpop), "people in the US.")