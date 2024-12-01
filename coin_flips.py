#import random module in to main prog
import random

#two variable to ask the user for number of coin flips and probility of the coin landing on heads
#flips has to be integer value
times = int(input("Enter the number of times to flip the coin "))
#probability has to be a float value
prob = float(input("Enter the probability that the coin lands heads side up as a decimal "))


#begin values and running counts for the amount of heads landing and tails landing in the while function and the starting value for flips
times_= 1
heads = 0
tails = 0

#while function to have the inside code repeat the amount of times the user inputs
while times_ <= times:
    #random floating number between 0 and 1 to the variable flip
    flip = random.random()
    #if statement when the coin is flipped, any number under the prob. inputted by user will be heads
    #can be bias coin flip for heads if inputted probability is greater than 0.5
    if flip < prob:
        #if so add 1 to the running count
        heads = heads + 1
    #else statement where if anything else is tail
    else:
        # if so add 1 to the running count
        tails = tails + 1
    #after running code add one to the running count for the number of flips
    times_ = times_ + 1


#main prog.
#print the amount time heads and tails landed
print("Heads has landed", heads, "times and Tails has landed", tails, "times")