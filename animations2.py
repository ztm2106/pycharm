#tell python we wnt to use the pygame module
import color
import pygame
import pygame_helper

#get the prog. ready for drawing graphics
#init is a abbrv. for initalize
pygame.init()

#dimensions of the window
side = 500

#this creates a new pygame window
#double parentheses
win = pygame.display.set_mode((side, side))

#fill the full window with using fill method that is part of the win object
win.fill(color.white)
pygame.display.update()
pygame_helper.wait_for_click()
#draw a circle at top of the cneter of win that fills 1/10 the height of the win

radius = side // 20
x = radius
y = side // 2
pygame.draw.circle(win, color.black, (x, y), radius)

#moive ball down middle
#while funct. to repeat code for circles
#checks if y value is less than the side for y
while x < side - radius:
    #before we draw the cricle, clear the win
    win.fill(color.white)

    pygame.draw.circle(win, color.black, (x, y), radius)
    #change y and draw next circle
    x = x + 1
    pygame.display.update()
    pygame.time.delay(5)
#when condition is no longer true continue to main prog

while y > 0 + radius:
    #before we draw the cricle, clear the win
    win.fill(color.white)

    pygame.draw.circle(win, color.black, (x, y), radius)
    #change y and draw next circle
    y = y - 1
    pygame.display.update()
    pygame.time.delay(5)

while y < side - radius:
    #before we draw the cricle, clear the win
    win.fill(color.white)

    pygame.draw.circle(win, color.blue, (x, y), radius)
    #change y and draw next circle
    y = y + 1
    x = x - 1
    pygame.display.update()
    pygame.time.delay(5)

while y > 0 + radius:
    #before we draw the cricle, clear the win
    win.fill(color.white)

    pygame.draw.circle(win, color.blue, (x, y), radius)
    #change y and draw next circle
    y = y - 1
    pygame.display.update()
    pygame.time.delay(5)