#adding up numbers using a loop

n = int(input("Enter a number: "))

i = 1

#make variable to store sum

sum = 0

#keep looping while counting varible the user gave us
while i <= n:
    #add i to sum
    #sum = sum + 1
    sum += i

    #i = i + 1
    i += 1

print(sum)