
#define a function for converting user input number of character and length of the password to
# the total number of passwords up to length n using chars possible characters
def num_password(_chars, _n):
    """
    :param _chars:
    :param _n:
    :return: the total number of passwords up to length n
    """
    #starting variable there has to be at least one character for a pass
    i = 1
    #with no character the starting total is 0
    total = 0

    # loop from 1 to _n inputted by user
    while i <= _n:
        # add the number of password to running total
        total = total + (_chars ** i)
        # increment i up to _n
        i = i + 1
#when while function is false print the _n, _chara and total values on console
    print("The total number of passwords up to length", _n, "using", _chars, "possible characters is", total,".")

#calling function in main program to find out the number of password from 94 characters and length of 2
num_password(94, 2)
