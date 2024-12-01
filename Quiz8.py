#we can use for loops to help us generate truth tables for various logical operators
#and
#for loops can aslo iterate through the values of a tuple
print("X","\t\t","Y","\t\t", "not X", "\t", "not Y", "\t", "X and Y", "\t", "X or Y", "\t", "not X and not Y", "\t", "not X or not Y")
print("===================================================================================================")
for x in (True, False):
    for y in (True, False):
        print(x, "\t", y, "\t", not x, "\t", not y, "\t", x and y, "\t\t", x or y, "\t\t", not x and not y, "\t\t\t\t", not x or not y)