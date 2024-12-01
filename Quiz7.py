

#for loop to repeat 1 from 1 - 100 in 1 increments
for i in range(1, 101, 1):
    #if divisible by 3 print
    if i % 3 == 0:
        print("oh")
    # if divisible by 5 print
    elif i % 5 == 0:
        print("no")
    # if divisible by 3 and print
    elif i % 3 == 0 and i % 5 == 0:
        print("oh no")
    #if not divisible by 3 or/and 5 than print the number
    else:
        print(i)

