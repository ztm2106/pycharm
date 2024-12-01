#use pygame and nested loops to generate a gradient
import pygame
import pygame_helper

pygame.init()
#window with dimensions
width = 600
height = 600
win = pygame.display.set_mode((width, height))

pygame_helper.wait_for_click()

#we can use nested loops to go through all x-y coord. in the window
for y in range(height):
    for x in range(width):
        #x-y will be a unique coord. in the wind
        #we can mulitply 255 by the propor. of the horizontal
        #position to our color
        val = 160 * x // width
        val2 = 160 * x // width
        val3 = 160 * x // width
        #gray colors have the same RGB values
        win.set_at((x, y), (val, val2, val3))
    pygame.display.update()

pygame_helper.wait_for_click()