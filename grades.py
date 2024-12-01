#analysis of collecton of grade

def average(grades):
    """
    compute and return average of an collection of grades
    :param grades:sequence (tuple or list) of grades vals
    :return: the average of the grade
    """
    #to calcuate average
    #1. add up all numbers
    total = 0
    for g in grades:
        total += g
    avg = total / len(grades)
    return avg

    #2. divide by the total number of grades

def median(grades):
    """
    compute the middle element of the list of grades
    :param grades: (list) of grades
    :return: the middle value
    """

    #grades need to be in a sorted order to find the middle element
    grades.sort()

    #if the length of the data is odd, return the middle value
    #otherwise return the average of the two middle values

    if len(grades) % 2 == 0:
        #even
        mid1 = grades[len(grades) // 2]
        mid2 = grades[len(grades) // 2 - 1]
        return (mid1 + mid2) / 2
    else:
        return grades[(len(grades)- 1) // 2]


#main prog

grades_tuple = (98, 78, 72, 100, 85, 76, 88)

print("We are goig to computer the average for", len(grades_tuple), "grades.")
print("The third grade is: ", grades_tuple[2])
print("The average is", round(average(grades_tuple), 2))


#repeat the prog using lists
grades_list = [98, 78, 72, 100, 85, 76, 88, 23]
print("The average is", round(average(grades_list), 2))

grades_list[0] = int(input("Enter the updated grade for the first grade "))
print("The updated average is", round(average(grades_list), 2))

#add another val to list with apend
grades_list.append(35) #35 will be a new item at the end of list
print("The updated average is", round(average(grades_list), 2))

print("The median of this list is", median(grades_list))