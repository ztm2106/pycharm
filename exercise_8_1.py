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
#Using answer for Exercise 7 question 3, Draw the blue square relative to the gray square right bottom corner tip
side = height // 4
square_x = width // 2 - width // 8
square_y = height // 2 - height // 6
pygame.draw.rect(win, color.darkgrey, (square_x, square_y, side, side))

square4_x = square_x + side
square4_y = square_y + side
pygame.draw.rect(win, color.blue, (square4_x, square4_y, side, side))


#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()