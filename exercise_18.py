#random module
import random


#Ask the user for a start and stop number
start = int(input("Start Number: "))
stop = int(input("Stop Number: "))

#inital total and counter i
i = 0
total = 0
#while function to stop adding befor the last number in count
while i < stop-start:
    #adding the each number to the running total
    total = total + start + i
    #increment for counter
    i += 1
#main prog
print(total)

print("2======================")

#print saying before count down
print("T minus…")
#initial counter i, starting number for printing and
i = 0
s = 10
ns = 10
while i < s:
    print(ns)
    #increment for counter and counterdown
    ns -= 1
    i += 1
#main prog.
print("Liftoff!")

print("3======================")

#initial total and counter
i = 0
total = 0
#while function to repeat until 502
while i < 502:
    #running total
    total = total + i
    #increment
    i += 2
#main prog.
print(total)

print("4======================")

#initial tries, random number, and initial guess
guess = 0
rand_ = random.randrange(1,101)
x = 0
#while function to repeat until ==
while x != rand_:
    #user input there interger guess
    x = int(input("Guess Number: "))
    #increment
    guess += 1
#if statment if == so code and print writing with number of tries and randome number
if x == rand_:
    print("Yes! You guessed", guess, " many times and the random number was", rand_, "!")

print("5======================")

#keey track of how many times the body runs and done being False to start
count = 0
done = True
#while function to repeat random number between 0-1 while not done
while done:
    body = random.random()
    #count increment
    count += 1
    #if 0-.75
    if body < 0.75:
        print("hello")
    #anything else run this
    else:
        #change done to False
        done = False
#main prog
#print the how many times it loop
print("Body Looped", count, "time")







