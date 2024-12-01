#calc. a simple checksum from a number
#lets write this as a func.

def checksum(number):
    """
    Compute check sum from a number
    :param number: (int) use to compute checksum
    :return: (int) one digit from the sum of the digits
    """
    #keep track of the sum
    total = 0

    #the number will be 0 once we have removed all digits
    while number != 0:
        #get the ones place digit
        digit = number % 10
        # add the digits to our running total
        total = total + digit
        #remove the ones place
        number = number // 10
    #return the checksum; ones digit of the total
    return total % 10

#main prog.
n = int(input("Enter a number: "))
print(checksum(n))