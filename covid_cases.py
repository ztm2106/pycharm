import covid_data

print("List of Valid State")
print("=====================")

#list all proper states name that can be used
covid_data.print_states()
print("----------------------")

state = input("Choose and input the proper state name: ")

#validate the state inputted is correct
covid_data.valid_state(state)

print("\t","Date","\t","Number of Cases")
print("=================================")

#loop where id starts at 0 and runs until up to specific date
for id in range(covid_data.num_entries(state)):
    #find the date from module and save to date from the use of state input
    date = covid_data.date_by_entry_id(state, id)
    #using date and state to find cumulative cases on even date
    cases = covid_data.cases_on_date(state, date)
    #print both date and cass
    print(date, "\t", cases)