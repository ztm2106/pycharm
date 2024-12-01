#simplified version of the pong game
#animation of a ball bouncing around the screen
import color
import pygame
import pygame_helper
import random


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
    #did we hit paddle or right side wall
    #\ can be used to escape
    if x < paddle_x + paddle_w and \
            paddle_y <= y + ball_h // 1.5 <= paddle_y + paddle_h:
        #paddle
        #vertical position to line up with the paddle
        #horizontal position to line up with paddle
        #move the particle back to

        x = paddle_x + paddle_w
        dx = -dx


    elif x + ball_w >= side:
        #RIGHT SIDE
        x = side - ball_w
        dx = -dx

    elif x + ball_w <= 0:
        #LEFT SIDE
        x = side - ball_w
        dx = -dx

    elif y < 0:
        #top wall
        y = 0
        dy = -dy

    elif y + ball_h >= side:
        #bottom wall
        y = side - ball_h
        dy = -dy

    #ball collides with the barrier
    if barrier_x - ball_w < x < barrier_x + barrier_w and barrier_y - ball_h < y < barrier_y + barrier_h:
        #calculate ball c everytime x and y
        ball_c_y = ball_y + ball_h // 2
        ball_c_x = ball_x + ball_w // 2
        #calculate the width and y cords and height and x cord
        wy = (ball_w + barrier_w) * (ball_c_y - barrier_c_y)
        hx = (ball_h + barrier_h) * (ball_c_x - barrier_c_x)
        if wy > hx:
            #bottom of barrier
            if wy > -hx:
                y = barrier_y + barrier_h
                dy = -dy
            #left side of barrier
            else:
                x = barrier_x - ball_w
                dx = -dx
        else:
            #right side of barrier
            if wy > -hx:
                x = barrier_x + barrier_w
                dx = -dx
            #top of barrier
            else:
                y = barrier_y - ball_h
                dy = -dy
    #return to use in main prog
    return (x, y, dx, dy)


#initate the window
pygame.init()
#tell pygame to repeat the key process in ms
pygame.key.set_repeat(1, 10)
side = 600

#set a window
win = pygame.display.set_mode((side, side))

#fill win white
win.fill(color.white)

#update to show just white
pygame.display.update()

#load image
#ball is a surface object
ball = pygame.image.load("ball.png").convert_alpha()

#retrieve picture height and width
ball_w = ball.get_width()
ball_h = ball.get_height()



#random ball position or location
ball_x = random.randrange(150,600) - ball_w // 2
ball_y = random.randrange(0,600) - ball_h // 2

#load image of the paddle
paddle = pygame.image.load("paddle.png").convert_alpha()
paddle_w = paddle.get_width()
paddle_h = paddle.get_height()
#shift paddle 10 pixels in from the left
paddle_x = 10
#place in the middle of the vertically
paddle_y = side // 2 - paddle_h // 2
paddle_dy = 5



#move harizontall across the screen in a range between 2 sec ,4 sec randomly each game
ball_dx = side // random.randrange(2,4)
#move vertically across the screen in a range between 2,4 sec randomly each game
ball_dy = side // random.randrange(2,4)
pygame_helper.wait_for_click()
#creat a stop watch in pygame
clock = pygame.time.Clock()

#Bbarrier position and dimensions
barrier_x = 265
barrier_y = 200
barrier_w = 100
barrier_h = 250



#barrier has a steady center so it is in main program.
barrier_c_x = barrier_x + barrier_w // 2
barrier_c_y = barrier_y + barrier_h // 2




#player score count
player_1 = 0



#location of score on win
score_x = side // 2
score_y = side // 2

#font and size
font = pygame.font.SysFont("Veranda", 90)



#loop forever
while True:
    #clear out win
    win.fill(color.white)




    #barrier
    pygame.draw.rect(win, color.blue, (barrier_x, barrier_y, barrier_w, barrier_h))



    #Score
    if ball_x <= paddle_x + paddle_w and \
            paddle_y <= ball_y + ball_h // 1.5 <= paddle_y + paddle_h:
        #if hit paddle add 1 to score
        player_1 += 1








    #check if we lost
    if ball_x < 0:
        pygame_helper.wait_for_click()
        #print score in console
        print("Score: ", player_1)
        #the ball went off the screen
        #we lost quit game
        exit()






    #process all pygame events since the last loop iteration
    #pygame.event.get() returns the queue of event objects to process
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #user clicked red button to quit
            #python provides exit() to exti prog
            exit()
        #change ket press to mousemotion
        elif event.type == pygame.MOUSEMOTION:
            #set event position of mouse equal to (x,y) tuple
            m_x, m_y = event.pos
            #set y positions only to the tuple to just move paddle in y direction
            if m_y >= 0:
                paddle_y = m_y




    #ask the stopwatch how much time has gone by since we last ran the code
    #tick return the number of ms since the method last ran
    #divid by 1000 to get number of seconds
    #60 in the call to tick forces pygame to limit the frame rate animation to 60 fps
    time_elapsed = clock.tick(60) / 1000.0


    #move the ball
    ball_x, ball_y, ball_dx, ball_dy= move(ball_x, ball_y, ball_dx, ball_dy, time_elapsed)


    #draw the ball on the window
    win.blit(ball, (ball_x, ball_y))

    #check paddle is still in win
    if paddle_y < 0:
        paddle_y = 0
    elif paddle_y + paddle_h >= side:
        paddle_y = side - paddle_h


    #draw the ball on window
    win.blit(paddle,(paddle_x, paddle_y))

    # blit score
    score = font.render(str(player_1), True, color.purple)
    win.blit(score, (score_x, score_y))


    #update window
    pygame.display.update()





