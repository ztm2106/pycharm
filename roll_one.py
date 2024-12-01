#import random
import random


done = False

#keep a count of the rolls
count = 0

#loop while we have everything but one dice that landed on one
while not done:
    #roll again
    roll1 = random.randrange(1,7)
    roll2 = random.randrange(1,7)

    #keep track fo count
    count += 1

    #chech if we got one of the dice to land on one and the other didnt

    if roll1 == 1 and roll2 != 1 or roll1 != 1 and roll2 == 1:
       done = True
#main prog
print("We needed", count, "rolls to get a single dice to land the one side.")