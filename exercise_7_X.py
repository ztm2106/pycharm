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

#3
#Draw a dark gray square that is centered in the window and fills a quarter of the height of the window
side = height // 4
square_x = width // 2 - width // 12
square_y = height // 3
pygame.draw.rect(win, color.darkgrey, (square_x, square_y, side, side))

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



#5
#Draw the blue square relative to the gray square to the bottom side of the grey square from previous answer
side = height // 4
square_x = width // 2 - width // 12
square_y = height // 3
pygame.draw.rect(win, color.darkgrey, (square_x, square_y, side, side))

side = side
square3_x = square_x
square3_y = square_y + side
pygame.draw.rect(win, color.blue, (square3_x, square3_y, side, side))

#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()