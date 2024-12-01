#sum up the number of passwords from length 1 thru 10

#counting varible
i = 1

total = 0

#loop from 1 to 10
while i <= 10:
    print(i, 94**i)
    #add the number of password to pur running total
    total = total + 94**i
    #increment i
    i = i + 1

print("total =", total)

#math to see how long it would take to crack a password if we guess 10**9 password a second
print("It would take", (total // 10**9 // 3600 // 24 // 365), "years to crack the password")
