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

#1
#Draw a dark grey rectangle that fills half the horizontal
#space and a third of the vertical space in the window
#use variables to store width and height
rect_width = width // 2
rect_height = height // 3
rect_x = width // 2 - rect_width // 2
rect_y = height // 2 - rect_height // 2
pygame.draw.rect(win, color.darkgrey, (rect_x, rect_y, rect_width, rect_height))


#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()