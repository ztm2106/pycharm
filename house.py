#learning pygame shapes by drawing a house
#our basic setup for a pygame prog. that lets us generate comp. graphics

#tell python we wnt to use the pygame module
import pygame

#tell python to acces the pygame_helper module
import house
import pygame_helper

#import color module
import color

#I recommend putting functions after imports but before everything else

def butterfly(x, y, width, height):
    """
    draw a butterfly somewhere on the screen
    :param x: top left x coordinate
    :param y: top left y coordinate
    :param width: total distance from wingtip to wingtip
    :param height: total height of wing
    :return: None
    """""
    #draw left wing
    t1_pt1 = (x, y)
    t1_pt2 = (x + width // 2, y + height // 2)
    t1_pt3 = (x, y + height)
    #win is the global variable (it comes from main prog.)
    pygame.draw.polygon(win, color.purple, (t1_pt1, t1_pt2, t1_pt3))

    t2_pt1 = t1_pt2
    t2_pt2 = (x + width, y)
    t2_pt3 = (x + width, y + height)
    pygame.draw.polygon(win, color.purple, (t2_pt1, t2_pt2, t2_pt3))

    eb_x = x + width // 3
    eb_y = y
    eb_w = width // 3
    eb_h = height
    pygame.draw.ellipse(win, color.raspberry, (eb_x, eb_y, eb_w, eb_h))








#get the prog. ready for drawing graphics
#init is a abbrv. for initalize
pygame.init()

#dimensions of the window
width = 600
height = 500

#this creates a new pygame window
#double parentheses
win = pygame.display.set_mode((width, height))

#fill the full window with using fill method that is part of the win object
win.fill(color.blue)

#draw a rectangle that is 1/3 the height of the window
#1/3 the width of the window and is centered
r_width = width // 3
r_height = height // 3
r_x = width // 2 - r_width // 2
r_y = height // 2 - r_height // 2
pygame.draw.rect(win, color.yellow, (r_x, r_y, r_width, r_height))

#draw circle
c_radius = r_height // 6
c_x = r_x + r_width // 4
c_y = r_y + r_height // 2
pygame.draw.circle(win, color.lightgray, (c_x, c_y), c_radius)

# draw an ellipse
e_width = r_width // 4
e_height = r_height * 3 // 4
e_x = r_x + r_width * 3 // 4 - e_width // 2
e_y = r_y + r_height // 4
pygame.draw.ellipse(win, color.blue, (e_x, e_y, e_width, e_height))

# bottom of the door is just a rectangle overlapping the ellipse
door_bottom_width = e_width
door_bottom_height = e_height // 2
door_bottom_x = e_x
door_bottom_y = e_y + e_height // 2
pygame.draw.rect(win, color.blue, (door_bottom_x,
                                   door_bottom_y,
                                   door_bottom_width,
                                   door_bottom_height))

# to draw a triangle for the roof, we will need to
# create a polygon, or a set of points with lines
# drawn between them
tr_pt_0 = (r_x, r_y)
tr_pt_1 = (r_x + r_width//2, r_y - r_height // 2)
tr_pt_2 = (r_x + r_width, r_y)
pygame.draw.polygon(win, color.red, (tr_pt_0, tr_pt_1, tr_pt_2))

# draw lines on our window
pygame.draw.line(win, color.black,
                 (c_x, c_y - c_radius),
                 (c_x, c_y + c_radius),
                 c_radius // 5) # pixel width

pygame.draw.line(win, color.black,
                 (c_x - c_radius, c_y),
                 (c_x + c_radius, c_y),
                 c_radius // 5)

# if we add an optional final argument to any shape, it will
# draw an outline of that shape with the given thickness
pygame.draw.circle(win, color.black, (c_x, c_y), c_radius, c_radius // 5)

#draw butterfly
bf1_x = width // 4
bf1_y = height // 4
bf1_w = width // 10
bf1_h = height // 10
butterfly(bf1_x, bf1_y, bf1_w, bf1_h)




#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()


