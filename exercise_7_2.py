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


#2
#Draw the blue rectangle relative to the gray rectangle with new variables using previous grey square
rect_width = width // 2
rect_height = height // 3
rect_x = width // 2 - rect_width // 2
rect_y = height // 2 - rect_height // 2
pygame.draw.rect(win, color.darkgrey, (rect_x, rect_y, rect_width, rect_height))

blue_width = width // 2.5
blue_height = rect_height
blue_x = width // 2 - rect_width // 4
blue_y = rect_y
pygame.draw.rect(win, color.blue, (blue_x, blue_y, blue_width, blue_height))



#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()