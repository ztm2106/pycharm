#Making a 2 player of Pong
#import the turtle module
import turtle
import os

#set window with turtle
wn = turtle.Screen()
#name the win
wn.title("Pong by Za")
#color the win
wn.bgcolor("black")
#set up the win width x and height y
wn.setup(width=800, height=600)
#  trace program execution, generate annotated statement coverage
#        listings, print caller/callee relationships and list functions executed during a program run
wn.tracer(0)


#Score
score_a = 0
score_b = 0


# Paddle A
#create new pcture inside the win for ball a
paddle_a = turtle.Turtle()
#set the speed for the paddle
paddle_a.speed(0)
#make paddle a square at fisr
paddle_a.shape("square")
#color the paddle
paddle_a.color("white")
#reshape the paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
#stop the the win from updating so we can update ourselves
paddle_a.penup()
#place paddle 350 from the middle of the win
paddle_a.goto(-350, 0)


# Paddle B
#create new pcture inside the win for paddle b
paddle_b = turtle.Turtle()
#set the speed for the paddle
paddle_b.speed(0)
#make paddle a square at fisr
paddle_b.shape("square")
#color the paddle
paddle_b.color("white")
#reshape the paddle
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
#stop the the win from updating so we can update ourselves
paddle_b.penup()
#place paddle 350 from the middle of the win
paddle_b.goto(350, 0)


# Ball
#create new pcture inside the win
ball = turtle.Turtle()
#set the speed for the paddle
ball.speed(0)
#make paddle a square at fisr
ball.shape("square")
#color the paddle
ball.color("white")
#stop the the win from updating so we can update ourselves
ball.penup()
#place paddle 350 from the middle of the win
ball.goto(0, 0)
#movement overtime
ball.dx = 0.5
ball.dy = -0.5

# Pen: writing the scores on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
# paddle moving up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    if paddle_a.ycor() > 260:
        y += 0
        paddle_a.sety(260)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    if paddle_a.ycor() < -240:
        y += 0
        paddle_a.sety(-240)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    if paddle_b.ycor() > 260:
        y += 0
        paddle_b.sety(260)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    if paddle_b.ycor() < -240:
        y += 0
        paddle_b.sety(-240)



#Keyboard Binding
# tell the full win to listen and follow new code
wn.listen()
# bind to a key on key board
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#Main game loop
while True:
    #update win after all code is run
    wn.update()

    #Move Ball
    #ball need to be updated for each movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    #bounce ball of the top and bottom
    # Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay pong_bounce.wav&")

    # Bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay pong_bounce.wav&")

    # if hit the right border go back to the center
        # and reverse direction
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        # clear what pen wrote
        pen.clear()
        # pen write again but with new score
        # .format corresponds to {} in string
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # if hit the left border go back to the center
        # and reverse direction
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay pong_bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay pong_bounce.wav&")








