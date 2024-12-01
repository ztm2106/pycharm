#tell python we wnt to use the pygame module
#import color module
#import pygame module
#tell python to acces the pygame_helper module
import color
import pygame
import pygame_helper


#define butterfly function to use in main prog consisting of two triangles and an oval
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
    pygame.draw.polygon(win, color.purple, (t1_pt1, t1_pt2, t1_pt3))
    #draw right
    t2_pt1 = t1_pt2
    t2_pt2 = (x + width, y)
    t2_pt3 = (x + width, y + height)
    pygame.draw.polygon(win, color.purple, (t2_pt1, t2_pt2, t2_pt3))
    #draw oval
    eb_x = x + width // 3
    eb_y = y
    eb_w = width // 3
    eb_h = height
    pygame.draw.ellipse(win, color.raspberry, (eb_x, eb_y, eb_w, eb_h))

#get the prog. ready for drawing graphics
#init is a abbrv. for initalize
pygame.init()

##dimensions of the window
width = 800
height = 600

#this creates a new pygame window
#double parentheses
win = pygame.display.set_mode((width, height))

#fill the full window with using fill method that is part of the win object
win.fill(color.dodgerblue1)

#rectangle for the lawn against the sky
lawn_width = width
lawn_height = height // 3
lawn_x = 0
lawn_y = height - height // 3
pygame.draw.rect(win, color.palegreen4, (lawn_x, lawn_y, lawn_width, lawn_height,))

#gray base house
base_house_width = width // 4
base_house_height = height // 4
base_house_x = width // 2 + width // 8
base_house_y = height // 2 + height // 25
pygame.draw.rect(win, color.gray38, (base_house_x, base_house_y, base_house_width, base_house_height))

#Multiple squarees for walkway in a curve like shape
walkway_1x = base_house_x + base_house_width // 2
walkway_1y = base_house_y + base_house_height + base_house_height // 10
walkway_1w = base_house_width // 2
walkway_1h = base_house_height // 8
pygame.draw.rect(win, color.gray21, (walkway_1x, walkway_1y, walkway_1w, walkway_1h))
pygame.draw.rect(win, color.black, (walkway_1x, walkway_1y, walkway_1w, walkway_1h), 5)

walkway_2x = base_house_x + base_house_width // 2.2
walkway_2y = base_house_y + base_house_height + base_house_height // 4
walkway_2w = base_house_width // 2
walkway_2h = base_house_height // 8
pygame.draw.rect(win, color.gray21, (walkway_2x, walkway_2y, walkway_2w, walkway_2h))
pygame.draw.rect(win, color.black, (walkway_2x, walkway_2y, walkway_2w, walkway_2h), 5)

walkway_3x = base_house_x + base_house_width // 2.6
walkway_3y = base_house_y + base_house_height + base_house_height // 2.5
walkway_3w = base_house_width // 2
walkway_3h = base_house_height // 8
pygame.draw.rect(win, color.gray21, (walkway_3x, walkway_3y, walkway_3w, walkway_3h))
pygame.draw.rect(win, color.black, (walkway_3x, walkway_3y, walkway_3w, walkway_3h), 5)

walkway_4x = base_house_x + base_house_width // 3.2
walkway_4y = base_house_y + base_house_height + base_house_height // 1.8
walkway_4w = base_house_width // 2
walkway_4h = base_house_height // 8
pygame.draw.rect(win, color.gray21, (walkway_4x, walkway_4y, walkway_4w, walkway_4h))
pygame.draw.rect(win, color.black, (walkway_4x, walkway_4y, walkway_4w, walkway_4h), 5)

walkway_5x = base_house_x + base_house_width // 4
walkway_5y = base_house_y + base_house_height + base_house_height // 1.4
walkway_5w = base_house_width // 2
walkway_5h = base_house_height // 8
pygame.draw.rect(win, color.gray21, (walkway_5x, walkway_5y, walkway_5w, walkway_5h))
pygame.draw.rect(win, color.black, (walkway_5x, walkway_5y, walkway_5w, walkway_5h), 5)

# black door : rectangle and circle for the a top curve with a rectangle going vertical on the door to show it open
door_rect_width = base_house_width // 4
door_rect_height = base_house_height - base_house_height // 2.9
door_rect_x = base_house_x + base_house_x // 4
door_rect_y = base_house_y + base_house_y // 6
pygame.draw.rect(win, color.black, (door_rect_x, door_rect_y, door_rect_width, door_rect_height))
        #top of door  window back ground
top_of_door_radius = door_rect_width // 2
top_of_door_x = door_rect_x + door_rect_width // 2
top_of_door_y = door_rect_y
pygame.draw.circle(win, color.black, (top_of_door_x, top_of_door_y), top_of_door_radius)
        # top of the door window
top_of_door_o_radius = door_rect_width // 2.6
top_of_door_o_x = door_rect_x + door_rect_width // 2
top_of_door_o_y = door_rect_y
pygame.draw.circle(win, color.paleturquoise1, (top_of_door_o_x, top_of_door_o_y), top_of_door_o_radius)
                #darkgrey second door layer for design
door_rect_o_width = door_rect_width - door_rect_width // 8
door_rect_o_height = door_rect_height - door_rect_height // 20
door_rect_o_x = door_rect_x + door_rect_x // 200
door_rect_o_y = door_rect_y + door_rect_y // 200
pygame.draw.rect(win, color.darkgrey, (door_rect_o_x, door_rect_o_y, door_rect_o_width, door_rect_o_height))
                #black third door layer for design
door_rect_o2_width = door_rect_o_width - door_rect_o_width // 8
door_rect_o2_height = door_rect_o_height - door_rect_o_height // 20
door_rect_o2_x = door_rect_o_x + door_rect_o_x // 200
door_rect_o2_y = door_rect_o_y + door_rect_o_y // 200
pygame.draw.rect(win, color.black, (door_rect_o2_x, door_rect_o2_y, door_rect_o2_width, door_rect_o2_height))
                #darkgrey fourth door layer for design
door_rect_o3_width = door_rect_o2_width - door_rect_o2_width // 8
door_rect_o3_height = door_rect_o2_height - door_rect_o2_height // 20
door_rect_o3_x = door_rect_o2_x + door_rect_o2_x // 200
door_rect_o3_y = door_rect_o2_y + door_rect_o2_y // 200
pygame.draw.rect(win, color.darkgrey, (door_rect_o3_x, door_rect_o3_y, door_rect_o3_width, door_rect_o3_height))
                #black fifth door layer for design
door_rect_o4_width = door_rect_o3_width - door_rect_o3_width // 8
door_rect_o4_height = door_rect_o3_height - door_rect_o3_height // 20
door_rect_o4_x = door_rect_o3_x + door_rect_o3_x // 200
door_rect_o4_y = door_rect_o3_y + door_rect_o3_y // 200
pygame.draw.rect(win, color.black, (door_rect_o4_x, door_rect_o4_y, door_rect_o4_width, door_rect_o4_height))
                        #white middle of the door lining design
line_open_door_width = door_rect_width // 25
line_open_door_height = door_rect_height
line_open_door_x = door_rect_x + door_rect_width // 2
line_open_door_y = door_rect_y
pygame.draw.rect(win, color.white,(line_open_door_x, line_open_door_y, line_open_door_width, line_open_door_height))
                                #gold door knob for the right side door
door_knob_radius = door_rect_width // 15
door_knob_x = door_rect_x + door_rect_width - door_rect_width // 3
door_knob_y = door_rect_y + door_rect_height // 2
pygame.draw.circle(win, color.gold1, (door_knob_x,door_knob_y), door_knob_radius)



#Top part of base house
    #whiteshells triangle roof on right half of the base house
roof_x = base_house_x + base_house_width // 2
roof_y = base_house_y
tr_pt_0 = (roof_x, roof_y)
tr_pt_1 = (roof_x + base_house_x // 3, roof_y)
tr_pt_2 = (roof_x, roof_y - base_house_y // 2)
pygame.draw.polygon(win, color.seashell1, (tr_pt_0, tr_pt_1, tr_pt_2))
        #circle window in the miidle of of the triangle roof
roof_window_radius = door_rect_width // 1.7
roof_window_x = roof_x + base_house_x // 2 // 5
roof_window_y = roof_y - base_house_y // 2 // 3.5
pygame.draw.circle(win, color.paleturquoise1, (roof_window_x, roof_window_y), roof_window_radius)
        #window frames
        #circle frames
roof_window_o_radius = door_rect_width // 1.7
roof_window_o_x = roof_x + base_house_x // 2 // 5
roof_window_o_y = roof_y - base_house_y // 2 // 3.5
roof_border = 3
pygame.draw.circle(win, color.black, (roof_window_o_x, roof_window_o_y), roof_window_o_radius, roof_border )
        #lines for frmae
pygame.draw.line(win, color.black, (roof_window_x, roof_window_y - roof_window_radius), (roof_window_x, roof_window_y + roof_window_radius), 3)
pygame.draw.line(win, color.black, (roof_window_x - roof_window_radius, roof_window_y), (roof_window_x + roof_window_radius, roof_window_y), 3)




#tress on the right on the base house
    #darker brown medium tree
tree1_width = width // 20
tree1_height = height // 2.5
tree1_x = width // 2 // 2 // 6
tree1_y = height // 2
pygame.draw.rect(win, color.sepia, (tree1_x, tree1_y, tree1_width, tree1_height))
    #lighter brown small tree
tree2_width = width // 15
tree2_height = height // 3
tree2_x = width // 2 // 2 // 2
tree2_y = height // 2 + height // 20
pygame.draw.rect(win, color.chocolate4, (tree2_x, tree2_y, tree2_width, tree2_height))
    #darker brown biggest tree
tree3_width = width // 15
tree3_height = height // 2.5
tree3_x = width // 2 // 2
tree3_y = height // 2 + height // 100
pygame.draw.rect(win, color.sepia, (tree3_x, tree3_y, tree3_width, tree3_height))
        #circle leaves for the trees
        #middle tree with orange leaves
leaves2_radius = height // 6
leaves2_x = tree2_x + tree2_width // 2
leaves2_y = tree2_y
pygame.draw.circle(win, color.orangered2, (leaves2_x, leaves2_y), leaves2_radius)
        #right tree with lighter green leaves
leaves3_radius = height // 5
leaves3_x = tree3_x + tree3_width // 2
leaves3_y = tree3_y - tree3_width // 2 - tree3_width // 2
pygame.draw.circle(win, color.sgichartreuse, (leaves3_x, leaves3_y), leaves3_radius)
        #left tree with dark green leaves
leaves1_radius = height // 6
leaves1_x = tree1_x + tree1_width // 2
leaves1_y = tree1_y
pygame.draw.circle(win, color.forestgreen, (leaves1_x, leaves1_y), leaves1_radius)





#rectangle for elevator to a separate sky house
elev_width = width // 10
elev_height = height // 2.6
elev_x = width // 2
elev_y = height // 3
pygame.draw.rect(win, color.seashell4, (elev_x, elev_y, elev_width, elev_height))

#rectangle for elevator to a separate sky house
elev_width = width // 10
elev_height = height // 2.6
elev_x = width // 2
elev_y = height // 3
pygame.draw.rect(win, color.seashell4, (elev_x, elev_y, elev_width, elev_height))

elev_door_width = width // 11.5
elev_door_height = height // 8
elev_door_x = elev_x + elev_width // 12.5
elev_door_y = elev_y + elev_height // 2 + elev_height // 6
pygame.draw.rect(win, color.paleturquoise1, (elev_door_x, elev_door_y, elev_door_width, elev_door_height))
        #add outlines
pygame.draw.rect(win, color.black, (elev_door_x, elev_door_y, elev_door_width, elev_door_height), 6)
pygame.draw.line(win, color.black, (elev_door_x + elev_door_width // 2, elev_door_y), (elev_door_x + elev_door_width // 2, elev_door_y + elev_door_height), 3)





#sky house off of elevator
#sky house
sky_width = 4 * elev_width
sky_height = elev_height // 2 + elev_height // 4
sky_x = elev_x - 2.2 * elev_width
sky_y = elev_y - sky_height
pygame.draw.rect(win, color.paleturquoise1, (sky_x, sky_y, sky_width, sky_height))

#Z decoration in sky house
pygame.draw.line(win, color.darkslateblue, (sky_x + sky_width // 6, sky_y + sky_height // 6), (sky_x + sky_width // 3, sky_y + sky_height // 6), 10)
pygame.draw.line(win, color.darkslateblue, (sky_x + sky_width // 6, sky_y + sky_height // 2), (sky_x + sky_width // 3, sky_y + sky_height // 6), 12)
pygame.draw.line(win, color.darkslateblue, (sky_x + sky_width // 6, sky_y + sky_height // 2), (sky_x + sky_width // 3, sky_y + sky_height // 2), 10)

#inside house
    #picture
    # canvas with frame
art_width = sky_width // 4
art_height = sky_height // 3
art_x = sky_x + sky_width - sky_width // 2.5
art_y = sky_y + sky_height // 8
pygame.draw.rect(win, color.white, (art_x, art_y, art_width, art_height))
pygame.draw.rect(win, color.raspberry, (art_x, art_y, art_width, art_height), 3)
        #artwork shapes in picture
            #circle
circ_a_radius = art_width // 8
circ_a_x = art_x + art_width // 4
circ_a_y = art_y + art_height // 4
pygame.draw.circle(win, color.thistle, (circ_a_x, circ_a_y), circ_a_radius)
            #rectangle
rect_a_width = art_width // 3
rect_a_height = art_height // 5
rect_a_x = art_x + art_width // 3
rect_a_y = art_y + art_height - art_height // 3
pygame.draw.rect(win, color.turquoise4, (rect_a_x, rect_a_y, rect_a_width, rect_a_height))
            #ellipse
ellipse_a_width = art_width // 4
ellipse_a_height = art_height // 7
ellipse_a_x = art_x + art_width - art_width // 3
ellipse_a_y = art_y + art_height // 4
pygame.draw.ellipse(win, color.blue, (ellipse_a_x, ellipse_a_y, ellipse_a_height, ellipse_a_width))

    #walk way in sky house
sky_base_width = sky_width
sky_base_height = sky_height // 4
sky_base_x = sky_x
sky_base_y = sky_y + sky_height - sky_height // 4
pygame.draw.rect(win, color.burlywood4, (sky_base_x, sky_base_y, sky_base_width, sky_base_height))

#black sky house outline
pygame.draw.rect(win, color.black, (sky_x, sky_y, sky_width, sky_height), 5)

#sky house door
sky_door_width = sky_width // 6
sky_door_height = sky_height // 2
sky_door_x = sky_x + sky_width // 2 + sky_width // 4 + sky_width // 15
sky_door_y = sky_y + sky_height // 2 + sky_height // 200
pygame.draw.rect(win, color.black, (sky_door_x, sky_door_y, sky_door_width, sky_door_height))

#two gold sky house door knob symmetrical about sky door
sky_knob_radius = door_rect_width // 15
sky_knob_x = sky_door_x + sky_door_width - sky_door_width // 3
sky_knob_y = sky_door_y + sky_door_height // 2
pygame.draw.circle(win, color.gold1, (sky_knob_x,sky_knob_y), sky_knob_radius)
#sky house gold doorknob
sky_knob_x = sky_door_x + sky_door_width // 3
pygame.draw.circle(win, color.gold1, (sky_knob_x,sky_knob_y), sky_knob_radius)

#use butterfly function at top to draw multiple butterflies
bw_x = width // 5
bw_y = height // 2
bw_w = width // 10
bw_h = height // 10
butterfly(bw_x, bw_y, bw_w, bw_h)

bw_x2 = width // 3
bw_y2 = height // 2 + height // 3
bw_w2 = width // 10
bw_h2 = height // 10
butterfly(bw_x2, bw_y2, bw_w2, bw_h2)

bw_x3 = width // 6
bw_y3 = height // 2 + height // 3.8
bw_w3 = width // 15
bw_h3 = height // 15
butterfly(bw_x3, bw_y3, bw_w3, bw_h3)

bw_x4 = width // 7
bw_y4 = height // 2.5
bw_w4 = width // 12
bw_h4 = height // 12
butterfly(bw_x4, bw_y4, bw_w4, bw_h4)

bw_x5 = width // 3.5
bw_y5 = height // 2 + height // 6
bw_w5 = width // 12
bw_h5 = height // 12
butterfly(bw_x5, bw_y5, bw_w5, bw_h5)


# the sun in the comprised of layers of yellow and orange
_1sun_x = 0
_1sun_y = 0
_1sun_r = height // 3
pygame.draw.circle(win, color.yellow, (_1sun_x, _1sun_y), _1sun_r)

_2sun_x = 0
_2sun_y = 0
_2sun_r = height // 4
pygame.draw.circle(win, color.orangered2, (_2sun_x, _2sun_y), _2sun_r)

_3sun_x = 0
_3sun_y = 0
_3sun_r = height // 5
pygame.draw.circle(win, color.yellow, (_3sun_x, _3sun_y), _3sun_r)

_4sun_x = 0
_4sun_y = 0
_4sun_r = height // 6
pygame.draw.circle(win, color.orangered2, (_4sun_x, _4sun_y), _4sun_r)


#tell pygame to update the display to show any cahnged we mad to the window
pygame.display.update()

#make the prog. wait until we click on the screen
pygame_helper.wait_for_click()



#1. Approximately how long did this assignment take you to complete?
#about 4 - 6 hours all together

#2. What was the most enjoyable part of this assignment?
#being able to be creativity and have full control of my vision

#3. Did you have any problems drawing your house? What solutions did you find for these
#problems? Were there any problems you couldn’t solve?
#At first I imported the house file to use a previous defined function for the butterflies.
# This would run all of the house file code and the code which brought up too different windows
#I took the defined function moved to this prog. above the init. string to not have the function in my code and only run this code
