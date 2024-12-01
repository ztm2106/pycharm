import pygame
import pygame_helper
import random
import color

def move(x, y):
    """
    Function to randomly move a particle to an adjacent pixel
    :param x: starting x cord
    :param y: staring y cord
    :return: (final x, final y)
    """
    #pick a random number range 1-8
    n = random.randrange(1,9)
    if n == 1:
        x -= 1
        y -= 1
    elif n == 2:
        y -= 1
    elif n == 3:
        x += 1
        y -= 1
    elif n == 4:
        x -= 1
    elif n == 5:
        x += 1
    elif n == 6:
        x -= 1
        y += 1
    elif n == 7:
        y += 1
    else:
        x += 1
        y += 1

    return (x,y)


#main prog.
pygame.init()

width = 600
height = 600
win = pygame.display.set_mode((width, height))

win.fill(color.white)

x = width // 2
y = height // 2

#counter to stop simulation
i = 0
while i < 10000000000000000:
    win.set_at((x,y), color.blue)

    (x,y) = move(x, y)

    #keep coords in win
    x %= width
    y %= height

    i += 1
    pygame.display.update()

pygame_helper.wait_for_click()