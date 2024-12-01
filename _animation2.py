#tell python we wnt to use the pygame module
import color
import pygame
import pygame_helper
import random

pygame.init()

width = 500
height = 600

#this creates a new pygame window
win = pygame.display.set_mode((width, height))
#fill the full window with using fill method that is part of the win object
win.fill(color.white)



#draw a circle at top of the cneter of win that fills 1/10 the height of the win

radius = height // 20
x = random.randrange(radius, width - radius)
y = random.randrange(radius, height -radius)
pygame.draw.circle(win, color.red, (x, y), radius)

move_right = True
move_down = True

pygame.display.update()
pygame_helper.wait_for_click()

#and operator to find if both conditions are true
#while x < width - radius and y < height - radius:

#loop forever
while True:
    #before we draw the cricle, clear the win
    win.fill(color.white)

    pygame.draw.circle(win, color.blue, (x, y), radius)
    if move_right:
        x = x + 1

    else:
        x = x - 1
    #runs if condition is false



    if move_down:
        y = y + 1


    else:
        y = y - 1



    if x >= width - radius:
        #set move right to false to no longer move right
        move_right = False


    if y >= height - radius:
        move_down = False

    if x <= radius:
        #set move right to false to no longer move right
        move_right = True

    if y <= radius:
        move_down = True

    pygame.display.update()
    pygame.time.delay(5)



pygame.display.update()
pygame_helper.wait_for_click()