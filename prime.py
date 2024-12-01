
#make a function to use in main prog.
def _prime(number):
    """
    Program to see if the user inputted number is prime
    :param x: user input number
    :return: True or false
    """
    #loop that goes from 2 -10 but not including 10
    #prime numbers are greater than 1
    if number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set found to False
                found = False
                #return found of true or false
                return found

#main prog.
#tell user to input an integer number to check
x = int(input("Enter a random integer: "))
#use user input in function to check of prime or not prime
d = _prime(x)

#use the returned True or False value
#if d is false the number is not prime becasue has a factor in the loop
if d == False:
    print(x, "is not prime")
#if not false than prime
else:
    print(x, "is prime")

