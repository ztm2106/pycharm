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
pygame.display.update()
pygame_helper.wait_for_click()
#draw a circle at top of the cneter of win that fills 1/10 the height of the win

radius = side // 20
x = side // 2
y = radius
pygame.draw.circle(win, color.black, (x, y), radius)

#moive ball down middle
#while funct. to repeat code for circles
#checks if y value is less than the side for y
while True:
    while y < side - radius:
        #before we draw the cricle, clear the win
        win.fill(color.white)

        pygame.draw.circle(win, color.black, (x, y), radius)
        #change y and draw next circle
        y = y + 1
        pygame.display.update()
        pygame.time.delay(1)
    #when condition is no longer true continue to main prog

    #move the ball to the left
    while x > 0 + radius:
        win.fill(color.white)
        pygame.draw.circle(win, color.red, (x, y), radius)

    #shift x to the left
        x = x - 1

        #update the display
        #pause 5 mill
        pygame.display.update()
        pygame.time.delay(1)

    #move ball up the left side of win
    while y > 0 + radius:
        win.fill(color.white)
        pygame.draw.circle(win, color.black, (x, y), radius)
            # change y and draw next circle
        y = y - 1
        pygame.display.update()
        pygame.time.delay(1)
        # when condition is no longer true continue to main prog


    #Move ball to the right on the top of win
    while x < side - radius:
        win.fill(color.white)
        pygame.draw.circle(win, color.red, (x, y), radius)
    #shift x to the left
        x = x + 1

        #update the display
        #pause 5 mill
        pygame.display.update()
        pygame.time.delay(1)

    #Down the right side of the win
    while y < side - radius:
        #before we draw the cricle, clear the win
        win.fill(color.white)

        pygame.draw.circle(win, color.black, (x, y), radius)
        #change y and draw next circle
        y = y + 1
        pygame.display.update()
        pygame.time.delay(1)




#tell pygame to update the display to show any cahnged we mad to the window
#make the prog. wait until we click on the screen
pygame.display.update()
pygame_helper.wait_for_click()