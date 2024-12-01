def sumPairs(a, b):
    """

    :param a: first list of integers
    :param b: second list of integers
    :return: list of the sums of these pairs
    """
    #create a new list to add to
    sum = []
    #loop to use indexes of lists
    for i in range(len(a)):
        #append to add to the open list every time to loops
        #i = 0, 1, 2, ...
        sum.append(a[i]+b[i])
    #return the new list
    return sum



# fill in function body



# M a i n   P r o g r a m


# Don't worry about how the main program works


# Test Sample Input 0
if sumPairs([5, 6, 7], [3, 6, 10]) == [8, 12, 17]:

    print("Sample Input 0 Passed")

else:

    print("Sample Input 0 Failed")

# Test Sample Input 1

if sumPairs((17, 28, 30, 5), (99, 16, 8, 88)) == [116, 44, 38, 93]:

    print("Sample Input 1 Passed")

else:

    print("Sample Input 1 Failed")

# Try your own inputs

print("Enter your own numbers on one line (separated by spaces)")

a = [int(x) for x in input("A:").split()]

b = [int(x) for x in input("B:").split()]

print(sumPairs(a, b))