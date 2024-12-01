import pygame
import pygame_helper
import color

pygame.init()

width = 600
height = 500

win = pygame.display.set_mode((width, height))

win.fill(color.white)

#create font object
font = pygame.font.SysFont("Veranda", 60)

#render some text into a new surface
#True == enable anti-aliasing to smooth edges of text
msg = font.render("We Love You Minh!!!!!", True, color.purple)

#blit message to win -----> centered
msg_w = msg.get_width()
msg_h = msg.get_height()
msg_x = width // 2 - msg_w // 2
msg_y = height // 2 - msg_h // 2
win.blit(msg, (msg_x, msg_y))

#update and pause
pygame.display.update()
pygame_helper.wait_for_click()

