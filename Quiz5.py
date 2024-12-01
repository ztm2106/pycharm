#computes the sum of cubes from 1 to 10

#inital starting point is 1
i = 1
#beginning total of sums of cube at i = 0
total = 0
#while function where i is less than or equal to 10 that max number
while i <= 10:
    #running total for the sum of each cube
    total = total + (i ** 3)
    #i increment
    i = i + 1
#print the statement and total once i = 10
print("the sum of cubes from 1 to 10 is", total)