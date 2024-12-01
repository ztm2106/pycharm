#this will be like f_to_c but we will use our new function in util to convert the temp
import util

print(util.f2c(44))

fh = float(input("Enter a temp in F: "))
celsius = util.f2c(fh)

print(fh, "degrees F is", round(celsius, 1), "degrees C")