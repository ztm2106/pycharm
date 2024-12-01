#experiment with exponential growth and the world pop.

#ask the user for a year in the future to predict
target_year = int(input("Enter a year after 2017: "))

#figure out how many years after 2017 our target year is

years = target_year - 2017

#years tell us how many times we need to repeat our pop. growth
#estimate

#starting pop. in 2017 (7.5 billion)
P = 7.5e9

#counting variable
n = 1

#store the growth rate
r = 1.0111
#repeat estimate until n == years
while n <= years:
    #update population
    P = r * P
    #the growth decreases by (0.00025) every year
    r = r - 0.00025
    #increment n
    n = n + 1

print("In", target_year, "the pop. is estimated to be", round(P, 0))