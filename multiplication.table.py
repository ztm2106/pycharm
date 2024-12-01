#use nested loops to generate a 10x10 multiplication table

#outer loop will iterate through the rows of values
for i in range(1,11):
    #inner loop to iterate through the columns in the row
    for j in range(1,11):
        #print product if i and j
        #end= is a "named parameter" and it i the data that gets printed after all other arguments (defalut: \n
        print(i * j, end="\t")

    #befroe next row print new line
    print()