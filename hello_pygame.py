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

#this creates a new pygame window
#double parentheses
win = pygame.display.set_mode((600, 600))

#fill the full window with using fill method that is part of the win object
win.fill(color.blue)

#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()


