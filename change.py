#Given an amount of money, computer the bills and coins need to produec this amount of money

#ask user for an amount of money
amount = float(input("Enter amount of money here: "))

#compute change

#Integer division to determine number of bills/coins
#mod to determine the left over amount
#reuse same amount varibale since we dont need the old amount
#on the right side of the assigned operator (=) amount is still old value but is being overwritten

#20s
twenties = amount // 20
amount = amount % 20

#10s
tens = amount // 10
amount = amount % 10

#5s
fives = amount // 5
amount = amount % 5

#1s
ones = amount // 1
amount = amount % 1

#.25
twentyfivecents = amount // .25
amount = amount % .25

#.10
tencents = amount // .10
amount = amount % .10

#.05
fivecents = amount // .05
amount = amount % .05

#Cant go lower than a pennie but .01s
onecent = amount // .01


#print result of each size of money dtermining amount

print(twenties, "$20 bills")
print(tens, "$10 bills")
print(fives, "$5 bills")
print(ones, "$1 bills")
print(twentyfivecents, "Quarters")
print(tencents, "Dimes")
print(fivecents, "Nickels")
print(onecent, "Pennies")