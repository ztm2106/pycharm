#blinking like stop light

import color
import pygame
import pygame_helper

pygame.init()

side = 500

win = pygame.display.set_mode((side, side))

win.fill(color.white)
pygame.display.update()
pygame_helper.wait_for_click()


radius = side // 20
x = side // 2
y = radius
pygame.draw.circle(win, color.black, (x, y), radius)


while y < side - radius:



    pygame.draw.circle(win, color.black, (x, y), radius)
    pygame.time.delay(1000)
    pygame.display.update()
    pygame.time.delay(1000)
    win.fill(color.white)
    pygame.display.update()

    y = y + radius * 2

    pygame.draw.circle(win, color.blue, (x, y), radius)
    pygame.time.delay(1000)
    pygame.display.update()
    pygame.time.delay(1000)
    win.fill(color.white)
    pygame.display.update()

    y = y + radius * 2

    pygame.draw.circle(win, color.red, (x, y), radius)
    pygame.time.delay(1000)
    pygame.display.update()
    pygame.time.delay(1000)
    win.fill(color.white)
    pygame.display.update()

    y = y + radius * 2

    pygame.draw.circle(win, color.green, (x, y), radius)
    pygame.time.delay(1000)
    pygame.display.update()

    y = y + radius * 2



pygame.display.update()
pygame_helper.wait_for_click()