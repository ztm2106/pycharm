def miniMaxSum(arr):
    """
    Given a list of N integers, find the minimum and maximum value that can be calculated by summing exactly N-1 of the values.
    :param arr:a list of N integers
    :return:a tuple where the first item is the minimum sum and the second item is the maximum sum.
    """
    # keep total for next loop
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        for g in range(len(arr)):
            #maximum total with 4 values in list
            if total - arr[g] > total - arr[g-1]:
                a = total - arr[g]
            #minimum total with 4 values in list
            if total - arr[g] < total - arr[0]:
                b = total - arr[g]
    #put into tupple
    minimax = (b, a)
    #return the tuple
    return minimax




# fill in function body


# M a i n   P r o g r a m


if miniMaxSum([7, 9, 3, 1, 5]) == (16, 24):

    print("Sample Test 0 Passed")

else:

    print("Sample Test 0 Failed")

# Try your own list of numbers

print("enter all numbers on one line separated by spaces")

v = [int(x) for x in input("numbers: ").split()]

print(' '.join([str(x) for x in miniMaxSum(v)]))