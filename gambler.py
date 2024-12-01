#simulate a simple gambling game
import random

#Trackers
#start the players out with 1000 tokens
tokens = 1000
rounds = 0
#keep playing until they run out of money or doubles their winnings
while tokens > 0: #and tokens < 3000:
    #play one game... flip a coin
    if random.randrange(2) == 1:
        #lets consider 1 winning
        tokens += 1
    else:
        tokens -= 1
    #track the amount of games played
    rounds += 1
#what is true after while loops runs?
#tokens will either be0 and 2000
if tokens == 0:
    print("Drat...We lost all of our money")
else:
    print("Woohoo! We doubled")
print("This outcome took,", rounds, "rounds to complete")