#import random
import random


done = False

#keep a count of the rolls
count = 0

#loop while we have no snake eyes
while not done:
    #roll again
    roll1 = random.randrange(1,7)
    roll2 = random.randrange(1,7)

    #keep track fo count
    count += 1

    #chech if we got atleast 1 1

    if roll1 == 1 or roll2 == 1:
       done = True

print("We needed", count, "rolls to get a single 1.")

done = True

#keep a count of the rolls
count = 0

#loop while we have no snake eyes
while done:
    #roll again
    roll1 = random.randrange(1,7)
    roll2 = random.randrange(1,7)

    #keep track fo count
    count += 1

    #chech if we got snake eyes

    if roll1 == 1 and roll2 == 1:
       done = False

print("We needed", count, "rolls to get a snake.")