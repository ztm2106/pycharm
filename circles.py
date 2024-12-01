#draw 10 cricle down the middle of win

#learning pygame shapes by drawing a house
#our basic setup for a pygame prog. that lets us generate comp. graphics

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

#draw a circle at top of the cneter of win that fills 1/10 the height of the win

radius = side // 20
x = side // 2
y = radius
pygame.draw.circle(win, color.black, (x, y), radius)

#change y for next circle
y = y + 2 * radius
pygame.draw.circle(win, color.black, (x, y), radius)

#change y for next circle
y = y + 2 * radius
pygame.draw.circle(win, color.black, (x, y), radius)

#while funct. to repeat code for circles
#checks if y value is less than the side for y
while y < side:
    pygame.draw.circle(win, color.black, (x, y), radius)
    #change y and draw next circle
    y = y + 2 * radius
    pygame.display.update()
    pygame.time.delay(1000)

#when condition is no longer true continue to main prog


#tell pygame to update the display to show any cahnged we mad to the window
#make the prog. wait until we click on the screen
pygame.display.update()
pygame_helper.wait_for_click()