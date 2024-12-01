#tell python we want to use the math module
import math

#we can also ask the user for information on the values of the compound interest variables
C = float(input("Enter your initial amount invested "))
v = float(input("What is the yearly interest rate "))
t = float(input("How many year will it be until maturation "))
n = float(input("How times has the interest compounded per year "))

#using math in pythin to manipulate user input and follow the compound interest equation
r = v / 100
p = C * (1 + (r / n)) ** (t * n)

#print tells computer to output infomation
print("The value of the investment to the nearest penny is", round(p, 2), ".")