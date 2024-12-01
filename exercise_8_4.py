#tell python we wnt to use the pygame module
#import color module
#tell python to acces the pygame_helper module
import color
import pygame
import pygame_helper

#get the prog. ready for drawing graphics
#init is a abbrv. for initalize
pygame.init()

##dimensions of the window
width = 400
height = 300

#this creates a new pygame window
#double parentheses
win = pygame.display.set_mode((width, height))

#fill the full window with using fill method that is part of the win object
win.fill(color.lightgray)


#4
#Determine a reasonable center (x- and y-coordinate) and radius for this circle on the right upper side of window
x = width - width // 4
y = height // 4
radius = height // 8
pygame.draw.circle(win, color.darkgrey, (x, y), radius)

#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()