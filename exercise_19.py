#import random module
import random

print("1------------------------")

#ask user for a start and stop number
x = int(input("Start number: "))
y = int(input("Stop Number: "))
#running total of each number being asdd
num = 0
#for function where i ranges the two user inputs not adding the stop number
for i in range(x, y):
    #running total addition
    num += i
#main prog
#Print the start and stop numbers and total
print("The sum of", x, "through", y, ", not adding the last number is", num, ".")

print("2------------------------")

#print the statement
print("T minus...")
#for statemnt to repeat the code to count backwards from 10 to 1
for i in range(10, 0, -1):
    print(i)
#main prog
#print liftoff
print("Liftoff!")

print("3------------------------")

#running total
total = 0
#i repeats from 1-500
for i in range(501):
    #adds each number to running total
    total += i
#main prog
#print total fof 1-500
print("From 1- 500, the total is", total, ".")


print("4------------------------")

#initial total
total = 0
#i repeats from 1-10
for i in range(11):
    #roll defined by random number between 1-6
    roll = random.randrange(1, 7)
    #each roll being added to running total
    total += roll
#main prog
#print total of 10 roll of a 6 side dice
print("10 roll gets you a total of", total, ".")


