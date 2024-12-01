# program will prompt user for number of years and print the estimated population that many years from now

#variable to store current pop. value
pop = 38.2e7


#varialbe to prompt user and store data
years = float(input("Enter a number of years: "))


#math conversions to changes user input of years to seconds
#days
days = years * 365

#hours
hours = days * 24

#minutes
minutes = hours * 60

#seconds
seconds = minutes * 60

#change in birth, death, and new immigrants
#birth rate
birth = seconds/8

#death rate
death = seconds/12

#new immigrate rate
immigrant = seconds/33


#math conversion to calc. estimate population at year given from current pop.
newpop = pop + birth - death + immigrant



#print result of new estimate population
print("In", years, "the population will be about", int(newpop), "people!")
