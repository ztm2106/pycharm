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

#2
#Using answer for Exercise 7 question 3, Draw the blue square relative to the gray square center
#so that the blue square right top corner is in the center of the grey square
square_x = width // 2 - width // 8
square_y = height // 2 - height // 6
pygame.draw.rect(win, color.darkgrey, (square_x, square_y, side, side))

square2_x = square_x - side // 2
square2_y = square_y + side // 2
pygame.draw.rect(win, color.blue, (square2_x, square2_y, side, side))

#3
#Using answer Exercise 7 question 3, Draw the blue square relative to the gray square
#so that blue square on the left of the grey square and almost half of the side lenght up
square_x = width // 2 - width // 8
square_y = height // 2 - height // 6
#pygame.draw.rect(win, color.darkgrey, (square_x, square_y, side, side))

square3_x = square_x - side - side // 2
square3_y = square_y - side // 2 - side // 4
pygame.draw.rect(win, color.blue, (square3_x, square3_y, side, side))

#4
#Determine a reasonable center (x- and y-coordinate) and radius for this circle on the right upper side of window
x = width - width // 4
y = height // 4
radius = height // 8
pygame.draw.circle(win, color.darkgrey, (x, y), radius)

#5
#useing questiong 4 answer Determine a reasonable center (x- and y-coordinate) and radius for this circle on the right upper side of window
#and determine a blue circle same radius under and to the left of the grey circle not touching
x = width - width // 4
y = height // 4
radius = height // 8
pygame.draw.circle(win, color.darkgrey, (x, y), radius)

x2 = x - radius
y2 = y + (2 * radius)
pygame.draw.circle(win, color.blue, (x2, y2), radius)

#6
#using question 4 answer, draw a blue circle overlapping the grey circle that center is in the 4th quadrant of the grey circle
x = width - width // 4
y = height // 4
radius = height // 8
pygame.draw.circle(win, color.darkgrey, (x, y), radius)

x2 = x - radius // 1.5
y2 = y + radius // 1.5
pygame.draw.circle(win, color.blue, (x2, y2), radius)

#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()