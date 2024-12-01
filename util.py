#helpful utility functions we can use in other programs
import math

#define a function for converting degrees F to degrees C
import random


def f2c(f):
    '''
    Given a temp in F. calc the temp in C
    :param f: (float) temp in F
    :return: (float) temp in C
    '''
    c = 5 / 9 * (f -32)
    #stop running func and give back the data stored in local variable c
    return c


def c2a(r):
    '''
    
    :param r: (float) radius of circle 
    :return: (float) area of circle
    '''
    a = math.pi * (r ** 2)
    # stop running func and give back the data stored in local variable c
    return a


def h2v(h,r):
    '''
    :param h: (float) height of cone
    :param r: (float) radius of base circle
    :return: (float) volume of the cone
    '''
    v = (math.pi * (r ** 2) * (h / 3))
    # stop running func and give back the data stored in local variable c
    return v

def y2p(y):
    '''
    :param y: (float) years from now
    :return: (float) number of ppl in new pop
    '''
    # program will prompt user for number of years and print the estimated population that many years from now

    # variable to store current pop. value
    pop = 38.2e7

    # math conversions to changes user input of years to seconds
    # days
    days = y * 365

    # hours
    hours = days * 24

    # minutes
    minutes = hours * 60

    # seconds
    seconds = minutes * 60

    # change in birth, death, and new immigrants
    # birth rate
    birth = seconds / 8

    # death rate
    death = seconds / 12

    # new immigrate rate
    immigrant = seconds / 33

    # math conversion to calc. estimate population at year given from current pop
    np = pop + birth - death + immigrant
    # stop running func and give back the data stored in local variable c
    return np

def reverse(s):
    """
    Reverse string content
    :param s:  string of text
    :return: string reversed
    """
    rev = ""
    for i in s:
        #add first letter to the beginning of our new string
        rev = i + rev

    #return the full reversed string
    return rev

def scramble(s):
    """
    mix up string
    :param s: string to scramble
    :return: scrambled string
    """
    scram = ""
    while len(s) != 0:
        #pick arandom index in the word
        idx = random.randrange(len(s))

        #add charcter at this index to scram
        scram = scram + s[idx]

        #remove the charcter at the idx from s
        #get the sbstring up to the idx and xombine it with the substring 1 after the idx
        s = s[:idx] + s[idx + 1:]
    return scram
