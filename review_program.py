import random
print("Running 30 Times What Number or Even or Odd")
for i in range(31):
    x = random.randrange(100)
    if x % 2 == 0:
        print(i, x, "is Even")
        print("==================")
    else:
        print(i, x, "is Odd")
        print("==================")