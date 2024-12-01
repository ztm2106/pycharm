#defined a function max2 that returns the larger of the two parameters n,m inputted by user
def max2(n, m):
    """

    :param n: random number n input by user
    :param m: random number m input by user
    :return:

    """
    # if statement to show m is greater than parameter n
    if n <= m:
        # print the max value m
        print(m)
    #else statement if above if statement is false
    else:
        # print the max value n
        print(n)

#main prog
max2(9, 7)

#defined a function max3 that returns the maximum of three parameters x,y,z inputted by user
def max3(x, y, z):
    """

    :param x: random number x input by user
    :param y: random number y input by user
    :param z: random number z input by user
    :return:

    """
    #if statement using and statement to show z is greater than parameters x and y
    if x <= z and y <= z:
        #print the max value z
        print(z)
    # if statement using and statement to show y is greater than parameters x and z
    if x <= y and z <= y:
        # print the max value y
        print(y)
    # if statement using and statement to show x is greater than parameters y and z
    if y <= x and z <= x:
        # print the max value x
        print(x)

#main prog
max3(4, 2, 9)


#defined a function middle that returns the middle of three parameters c,v,b inputted by user
def middle(c, v, b):
    """

    :param c: random number c input by user
    :param v: random number v input by user
    :param b: random number b input by user
    :return:

    """
    #if statement using and statement to show v is greater than parameter c and less than parameter b
    if c <= v and v <= b:
        # print the middle value v
        print(v)
    #if statement using and statement to show c is greater than parameter v and less than parameter b
    if v <= c and c <= b:
        # print the middle value c
        print(c)
    #if statement using and statement to show b is greater than parameter v and less than parameter c
    if v <= b and b <= c:
        # print the middle value b
        print(b)

#main prog
middle(4, 1, 9)

