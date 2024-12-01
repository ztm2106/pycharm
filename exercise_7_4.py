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
#Draw the blue square relative to the gray square on the right side and use previous answer
side = height // 4
square_x = width // 2 - width // 12
square_y = height // 3
pygame.draw.rect(win, color.darkgrey, (square_x, square_y, side, side))

side = side
square2_x = square_x + side
square2_y = square_y
pygame.draw.rect(win, color.blue, (square2_x, square2_y, side, side))




#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()