def staircase(n):
    """
    create staircase with "#"s and " "s
    :param n: he size of the staircase
    :return: the print until range is met
    """
    #extend number to extend range to include n number of staircase
    x = n + 1
    for i in range(x):
        print(" " * (x-i-1) + "#" * (i))


# M a i n    P r o g r a m
#callling function int main prog. with only integer valuse allowed
staircase(int(input('n: ')))