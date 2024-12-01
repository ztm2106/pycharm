#simulate checking for duplicate birthday i a class of ppl
import random

#create a list of counts for each day pf the year and generate birthday for each virtual person, adding to the count of the day they have the birthday


#create a list and append 366 0s to its (

birthdays = []
for i in range(366):
    #note: counting leap year
    birthdays.append(0)

#birthdays [0] = jan 1st
#birthdays [365] = dec. 31st
num_people = 24
#loop over all people in the "room"
for i in range(num_people):
    #create a random birthday
    bday = random.randrange(366)
    #add 1 tot the count for that day
    birthdays[bday] += 1

#how can we tell that we have a duplicate
#one approach: sort numbers, check the last number
#if greater than 1, we ave at least one duplicate

birthdays.sort()
if birthdays[len(birthdays) - 1] > 1:
    print("There was a duplicate")
else:
    print("There we no duplicate ")