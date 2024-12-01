#visualize tokens won and lost by gambler
import pygame
import pygame_helper
import color
import random

#I recommend putting functions after imports but before everything else

#get the prog. ready for drawing graphics
#init is a abbrv. for initalize
pygame.init()

#dimensions of the window
width = 600
height = 600

#this creates a new pygame window
#double parentheses
win = pygame.display.set_mode((width, height))

#fill the full window with using fill method that is part of the win object
win.fill(color.white)

lx = 0
ly = 0 + width // 2


#draw red line
pygame.draw.line(win, color.red, (0, ly), (0+width, ly))

#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()




#start the gambling simulation
tokens = 0
round = 0

#keep track of number of rounds per horizontal pixel
rounds_per_pixel = 100
#play a number of rounds that fits horizontally
while round < width * rounds_per_pixel:
    if random.randrange(2) == 1:
        tokens += 1
    else:
        tokens -= 1

    win.set_at((round//rounds_per_pixel, height // 2 - tokens), color.blue)

    pygame.draw.line(win, color.red, (0, ly), (0+width, ly))
    pygame.display.update()
    round += 1

pygame_helper.wait_for_click()