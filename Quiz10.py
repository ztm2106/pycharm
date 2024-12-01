# a program that reads a number of names from user input and prints those names in sorted order
#Ask the user for the number of names to read.
num_of_names = int(input("Enter a number of names: "))

#Prompt the user the number of times listed above for a name.
list_of_names = []
for i in range(1, num_of_names + 1):
    x = input("Enter name: ")
    list_of_names.append(x)

#Sort the names provided by the user.
list_of_names.sort()

#Print each name on a separate line (in sorted order).
for g in range(len(list_of_names)):
    print(list_of_names[g])