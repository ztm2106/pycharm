import math

def draw_triangle(n):
    """

    :param n: number of asterisks to build triangle
    :return: triangle of astericks

    """
    #starting value for asterisks
    _i = 1
    # increasing by one until n *s
    # while funct. to repeat code for "*s"
    # checks if i value is less than the side for n
    while _i <= n:
        # print the math operations of each new _i and the "*"
        print("*" * _i)
        # change i and to print next set of *s
        _i = _i + 1

    # decreasing by one until back to 1 *
    # while funct. to repeat code for "*s"
    # checks if i value is greater than n
    while _i + n - 1 > n:
        # print the math operations of each new _i and the "*"
        print("*" * (_i - 2))
        #change i and to print next set of *s
        _i = _i - 1









