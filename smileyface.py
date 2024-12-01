#learning pygame shapes by drawing a house
#our basic setup for a pygame prog. that lets us generate comp. graphics

#tell python we wnt to use the pygame module
import pygame

#tell python to acces the pygame_helper module
import pygame_helper

#import color module
import color

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
win.fill(color.black)

#draw circle for smiley face base to touch the edges of win
c_radius = width // 2
c_x = c_radius
c_y = height // 2
pygame.draw.circle(win, color.yellow, (c_x, c_y), c_radius)

# draw an 2 same sized ellipse for smiley face eyes but symmetrical about the middle of the win
e_width = width // 8
e_height = height // 4
e_x = c_x - c_x // 2
e_y = c_y - c_y // 2
pygame.draw.ellipse(win, color.black, (e_x, e_y, e_width, e_height))

e_width = width // 8
e_height = height // 4
e_x = c_x + c_x // 4
e_y = c_y - c_y // 2
pygame.draw.ellipse(win, color.black, (e_x, e_y, e_width, e_height))

#outline of ellispe of mouth with the extra variable in tuple
mx = c_x - c_x // 2
my = c_y + c_y // 8
mh = e_height * 2
mw = e_width * 2
pygame.draw.ellipse(win, color.black, (mx, my, mh, mw), e_width // 10)

#rect to overlap half the outline of ellispes horizontally
r_width = mh
r_height = e_width

pygame.draw.rect(win, color.yellow, (mx, my, r_width, r_height))



#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()