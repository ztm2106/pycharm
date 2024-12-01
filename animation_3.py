#animation of a ball bouncing around the screen
import color
import pygame
import pygame_helper


def move(x, y, dx, dy, dt):
    """
    A function to move a particle based on the starting location and velocities
    :param x: current x coord
    :param y: current y coord
    :param dx: horizontal vel
    :param dy: vertical vel
    :param dt: time elapsed
    :return: (x,y, dx, dy) of the updated location and vel
    """

    x = x + dx * dt
    y = y + dy * dt
    #did we hit a side wall
    if x < 0:
        #left side
        x = 0
        dx = -dx
    elif x + ball_w >= side:
        #RIGHT SIDE
        x = side - ball_w
        dx = -dx

    if y <0:
        #top wall
        y = 0
        dy = -dy
    elif y + ball_h >= side:
        #bottom wall
        y = side - ball_h
        dy = -dy
    return (x, y, dx, dy)



pygame.init()
side = 600


win = pygame.display.set_mode((side, side))

win.fill(color.white)
#load image
#ball is a surface object
ball = pygame.image.load("ball.png").convert_alpha()

ball_w = ball.get_width()
ball_h = ball.get_height()

ball_x = side // 2 - ball_w // 2
ball_y = side // 2 - ball_h // 2

#move harizontall across the screen in 5 sec
ball_dx = side // 5
#move vertically across the screen in 3 sec
ball_dy = side // 3
pygame_helper.wait_for_click()
#creat a stop watch in pygame
clock = pygame.time.Clock()

#loop forever
while True:
    #clear out win
    win.fill(color.white)

    #ask the stopwatch how much time has gone by since we last ran the code
    #tick return the number of ms since the method last ran
    #divid by 1000 to get number of seconds
    #60 in the call to tick forces pygame to limit the frame rate animation to 60 fps
    time_elapsed = clock.tick(60) / 1000.0

    #move the ball
    ball_x, ball_y, ball_dx, ball_dy = move(ball_x, ball_y, ball_dx, ball_dy, time_elapsed)

    #draw the ball on the window
    win.blit(ball, (ball_x, ball_y))


    #update window
    pygame.display.update()





pygame.display.update()
pygame_helper.wait_for_click()