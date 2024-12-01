import color
import pygame
import pygame_helper

pygame.init()

# load image of bug
img = pygame.image.load("bug.jpg")

# get the dimensions of the image surface
width = img.get_width()
height = img.get_height()

# create a window of the same size
win = pygame.display.set_mode((width, height))

# ensure colors are correct
img = img.convert_alpha()

# create a font object to render text image surfaces
font = pygame.font.SysFont("Veranda", 60)

#set the message "hello" in white to msg and true bc i want it smooth
msg = font.render("Hello", True, color.white)

#get the width and height of the text and position text in the middle of win
msg_w = msg.get_width()
msg_h = msg.get_height()
msg_x = width // 2 - msg_w // 2
msg_y = height // 2 - msg_h // 2

#first blit image of bug
win.blit(img,(0,0))

#second blit the blac rectangle in the middle of pic
pygame.draw.rect(win, color.black, (msg_x - 3, msg_y - 5, msg_w + 6, msg_h + 6))

#third blit the msg "hello" on top of black rectangle
win.blit(msg, (msg_x, msg_y))

# update window and pause
pygame.display.update()
pygame_helper.wait_for_click()