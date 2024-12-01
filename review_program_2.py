
a = 0
numbers = []
while a >= 0:
    a = int(input("Enter a random number to add to list: "))
    if a >= 0:
        numbers.append(a)
    else:
        numbers.sort()
        print(numbers)



