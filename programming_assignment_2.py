#importing modules used for assignment
import pygame
import pygame_helper
import color
import covid_data

#intialize pygame
pygame.init()
#dimensions of window
height = 600
width = 600
#create pygame window
win = pygame.display.set_mode((width, height))
#window color
win.fill(color.gray21)


#coordinates for a line bottom of win
lx = 0
ly = 0
#draw black line for axises
pygame.draw.line(win, color.white, (lx, ly + height - 1), (lx+width, ly + height - 1))
pygame.draw.line(win, color.white, (lx, ly), (lx, ly + height))

title_x = 0
title_y = 0
font = pygame.font.SysFont("Veranda", 30)
title = font.render("COVID-19 Visualization", True, color.white)
win.blit(title, (title_x + width // 2 - width // 6, title_y + 10))

x_axis_label = font.render("Dates from March 01, 2020", True, color.yellow)
win.blit(x_axis_label, (title_x + width // 2 - width // 4, title_y + height - 30))

y_axis_label = font.render("Cumalative Cases/Deaths", True, color.orangered2)
z = pygame.transform.rotate(y_axis_label, 90)
win.blit(z, (title_x + 20, title_y + height // 2 - height // 4))



#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

print("List of Valid State")
print("=====================")

#list all proper states name that can be used
covid_data.print_states()
print("=====================")
#Ask the user to pick a state
state = input("Pick a state: ")
#validate the state inputted is correct
covid_data.valid_state(state)
#Ask the user if they wish to visualize cases or deaths
x = input("Do you wish to visualize the covid cases or deaths: ")

#for loop to loop through entry numbers and check if inputted value is cases or deaths
#save num entries of state inputted by user
num_entries = covid_data.num_entries(state)
for i in range(num_entries):
    # find the date from module and save to date from the use of state input
    date = covid_data.date_by_entry_id(state, i)
    # if user chose cases data
    if x == "cases":
        # using i and state to find cumulative cases on every date
        cases_on_date = covid_data.cases_by_entry_id(state, i)

        # x and y coordinate points
        # x axis == dates
        # y axis == cummulative cases
        # plotted death points are in green
        win.set_at((i * width // num_entries, height - cases_on_date * height // covid_data.cases_by_entry_id(state, covid_data.num_entries(state)-1)), color.blue)
        # update the win each loop to display plotted points
        pygame.display.update()

    # if user chose death data
    if x == "deaths":
        # using i and state to find cumulative deaths on every date
        deaths_on_date = covid_data.deaths_by_entry_id(state, i)

        #x and y coordinate points
        # x axis == dates
        #y axis == cummulative deaths
        #plotted death points are in red
        win.set_at((i * width // num_entries, height - deaths_on_date * height // covid_data.deaths_by_entry_id(state, covid_data.num_entries(state)-1)), color.red)
        #update the win each loop to display plotted points
        pygame.display.update()

#update win
pygame.display.update()
#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()

