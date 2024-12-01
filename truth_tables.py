#we can use for loops to help us generate truth tables for various logical operators

#and
#for loops can aslo iterate through the values of a tuple
print("X","\t\t","Y","\t\t", "X and Y","\t","X or Y")
print("============================================")
for x in (True, False):
    for y in (True, False):
        print(x,"\t",y,"\t",x and y, "\t\t", x or y)
