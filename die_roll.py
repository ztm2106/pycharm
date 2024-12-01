#roll a 6 sided die
import random

#randomly pick a side of the die
roll = random.randrange(1, 7)

if roll == 1:
    print("One")
elif roll == 2:
    print("Two")
elif roll == 3:
    print("Three")
elif roll == 4:
    print("Four")
elif roll == 5:
    print("Five")
else:
    print("Six")


