#define a function Num-digits with parameter numbers that is inputted by user

def num_digits(number):
    """
    #count the number of digits in a number inputted
    :param number: (int) use to compute checksum
    :return: (int) one digit from the sum of the digits
    """
    #the initial number og digits with no number entered
    total = 0
    #while function until number = 0
    while number != 0:
        #removes the 1 digit from the number entered and makes it the new number to go through while function
        number = number // 10
        #the running count of how many time this goes through signifying the number of digits
        total = total + 1
    #return function which gives the total which is the amount of digits
    return total
#variable enable a user to enter on integer number to use to understand the number of digits
n = int(input("Enter a number: "))
#print the answer to the defined function to the console with the user inputted number
print(num_digits(n))