#basic examples of for loops in python


print("Print the numbers 0-9")
#range(10) gives us a sequences of numbers from 0-9
#each number will be assigned to i as loop runs
for i in range(10):
    #print current value of i
    print(i)
print("-----------------------")

print("Add up the numbers 1 - 100")
#var to keep track of our total
total = 0
for i in range(101):
    #add the number the running total
    total = total + i
print(total)
print("-----------------------")

print("add up the numbers 12 - 26")
total = 0
for i in range(12,27):
    total += i
print(total)
print("-----------------------")



print("Examples from Notes")

sum = 0
for i in range(3,8,2):
    sum += i
print(sum)
print("-----------------------")

#count backwards
sum = 0
for i in range(8,3,-1):
    #go while i . stop
    sum += i
print(sum)
print("-----------------------")

print("Simple Examples of nested for loops")
for i in range(4):
    for j in range(3):
        print(i,j)
print("-----------------------")

print("A slightly more complicated nested for loop")
for i in range(4):
    for j in range(i,3):
        print(i,j)


print("-----------------------")

print("fpr loops can also loop over strings")
for c in "Inro to computer programming":
    #variable c will be assigned each character from the string
    print(c)

print("-----------------------")
print("for loops can also loop over a value in a tuple")
for value in (140, "Ayanda", (0,0)):
    #value variable will get each element of the tuple
    print(value)