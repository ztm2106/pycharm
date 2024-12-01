#tell python we wnt to use the pygame module
import color
import pygame
import pygame_helper

#get the prog. ready for drawing graphics
#init is a abbrv. for initalize
pygame.init()

#dimensions of the window
width = 600
height = 500
win = pygame.display.set_mode((width, height))

#this creates a new pygame window
#double parentheses
win.fill(color.white)

# draw a left black circle offset by its radius
radius = height // 8
x = width // 2 - radius
y = height // 2
pygame.draw.circle(win, color.black, (x, y), radius)

# draw right circle
circ2_x = x + 2 * radius
circ2_y = y
circ2_r = radius
# win is the global variable (it comes from main prog.)
pygame.draw.circle(win, color.yellow, (circ2_x, circ2_y), circ2_r)
#blue outline around yellow circle
pygame.draw.circle(win, color.blue, (circ2_x, circ2_y), circ2_r, 10)

# green line spaning from each circle center
pygame.draw.line(win, color.green, (x, y), (circ2_x, circ2_y), 10)




#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()
#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()