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
win.fill(color.lightgray)

#draw circle for smiley face base to touch the edges of win
c_radius = width // 2
c_x = c_radius
c_y = height // 2
pygame.draw.circle(win, color.yellow, (c_x, c_y), c_radius)

#draw an 2 same sized ellipse for face eyes balls  but symmetrical about the middle of the win
e_width = width // 8
e_height = height // 4
e_x = c_x - c_x // 2
e_y = c_y - c_y // 2
pygame.draw.ellipse(win, color.white, (e_x, e_y, e_width, e_height))

e_width = width // 8
e_height = height // 4
e_x2 = c_x + c_x // 4
e_y2 = c_y - c_y // 2
pygame.draw.ellipse(win, color.white, (e_x2, e_y2, e_width, e_height))


# 2 face eyes that are rolled up in the top middle of the previous ellipse
eye_x = e_x + e_x // 4
eye_y = e_y + e_y // 4
eye_radius = height // 20
pygame.draw.circle(win, color.black, (eye_x, eye_y), eye_radius)

eye_x = e_x2 + e_x2 // 10
eye_y = e_y2 + e_y2 // 4
eye_radius = height // 20
pygame.draw.circle(win, color.black, (eye_x, eye_y), eye_radius)


#rect to make a horizontal mouth ranging from both eyes and staying straight
rx = c_x - c_x // 2
ry = c_y + c_y // 3
r_width = c_radius
r_height = c_y // 10

pygame.draw.rect(win, color.black, (rx, ry, r_width, r_height))


#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()