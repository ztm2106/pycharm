import random

("Biased coin (9/11 but with floats")
flip = random.randrange(11)
if flip >= 9/11:
    print("Heads")
else:
    print("Tails")