#several examples of flipping coin
import random

#toss a coin
print("Fair coin (1/2 heads)")
flip = random.randrange(2)

if flip == 0:
    # when 0 will print heads
    print("heads")
else:
    #when anything else tails but this is 1
    print("tails")


#biased coin menas that one side is more likely to win
print("Biased coin (2/3 heads")
flip = random.randrange(3)
if flip >= 1:
    print("Heads")
else:
    print("Tails")

#we can also flip a boiased coin by choosing a float
print("Biased coin (2/3 but with floats")
flip = random.randrange(3)
if flip >= 2/3:
    print("Heads")
else:
    print("Tails")


#we can also use a random float to flip a fair coin
print("Fair coin (1/2 but with random float)")
flip = random.random()

if flip < 0.5:
    # when 0 will print heads
    print("heads")
else:
    #when anything else tails but this is 1
    print("tails")
