# Snake

import math
import random
import pygame
#use as to create alias for library for easier coding
#use from (library) import (module) to use specific module from the library
import tkinter as tk
from tkinter import messagebox

#cube objects for snacks and snake body
class cube(object):
    rows = 20
    w = 500

    #initially dirnx = 1 and dirny = 0 to have the snake start moving in the beginning
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    #used to move the cubes
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        #add the direction to the pos directions
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        #distance betwewn x and y values
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        #use the +1 and -2 to not cover the white lines on the grid of the win
        #inside of the squares
        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))

        if eyes:
            # center of the square
            centre = dis//3
            # radius for the eyes
            radius = 3
            # circle for the inner eyes
            circleMiddle = (i*dis+centre-radius, j*dis+8)
            circleMiddle2 = (i * dis + dis - radius*2, j * dis + 8)
            #draw the eyes with balck as the color
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)
#snake contains cubes for the body
class snake(object):
    #list for body of the cubes
    body = []
    #set or dictionary
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        #need to always know the position of the head
        self.head = cube(pos)
        #head of the snake is the starting pos and head is in list
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            for key in keys:
                #top left corner is (0,0)
                # x = -1 = left
                # x = 1 = right
                # y = -1 = up
                # y = 1 = down
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    #setting direction to the head of the snake
                    # [:] is a copy
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        # actually moving cube
        for i, c in enumerate(self.body):
            #grab positionn and see if
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                #giving the direction x and y
                c.move(turn[0], turn[1])
                #if we are on the lost cube we remove it
                #index of the list = len() function
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                #checking is we hit the edge of the screen
                #check if moving left then go to right screen
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                #check if moving right then go to tje left screen
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
                #check if moving down then go to bottom screen
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                # check if moving up then go to bottom screen
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows-1)
                #if nothing just move in given direction
                else: c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = ()
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        #knowing where to add cube to the body
        # if moving to the right and cube to left side
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1, tail.pos[1])))
        # if moving left add cube to the right side
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1, tail.pos[1])))
        # if moving up, dd cube to the bottom
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1]-1)))
        #if moving down, add cube to the top
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1]+1)))

        #set the direction for the new cube
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w, rows, surface):
    #size between each iteration to split up win
    sizeBtwn = w//rows

    x=0
    y=0
    #for loop to split up win
    for l in range(rows):
        x = x+sizeBtwn
        y = y+sizeBtwn

        #tell pygame to draw lines for each row; color is white with (255,255,255
        #vertically
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        #horizontal
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        #get filter list to see if any positons are the same as the snake body
        # make sure snack doesnt generate on snake
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            #if the same do it again
            continue
        else:
            break
    return (x,y)

#????????
def message_box(subject, content):
    #new tkinter window
    root = tk.Tk()
    #comes up on top of every other windows
    root.attributes("-topmost", True)
    #make window invisible
    root.withdraw()
    #shows the info
    messagebox.showinfo(subject, content)
    #tries to destroy the message box but actual destroys when game is quit
    try:
        root.destroy()
    except:
        pass



def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))
    snack = cube(randomSnack(rows, s), color = (0, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        #lower the number faster it updates
        pygame.time.delay(50)
        #snake moves 10 spaces per 1 sec
        clock.tick(10)
        #check if snake is moved or key is pressed
        s.move()
        #check if head of snake hit the snake
        #if hit add cube to the snake body
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))
        #check collision of snake
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
                print('Score: ', len(s.body))
                message_box('You Lost!','Play Again')
                s.reset((10,10))
                break
        #redraw the win after each iteration
        redrawWindow(win)
    pass

main()