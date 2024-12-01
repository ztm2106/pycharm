#transform an image in various ways

import color
import pygame
import pygame_helper

def darken(r, g, b):
    """
    darken a pixel 30%
    :param r: pixel value
    :param g: pixel value
    :param b: pixel value
    :return:
    """
    #reducing my 30% means multiplying by 70%
    r = int(r * 0.7)
    g = int(g * 0.7)
    b = int(b * 0.7)
    return (r, g, b)

def make_red(r,g,b):
    return (r, 0 , 0)

def shuffle(r,g,b):
    return (b,r,g)

def invert (r,g,b):
    #start from make instead of 0
    return(255 - r,255 - g,255 - b)

#converst color to greyscale
def greyscale(r, g, b):
    #add up the numbers
    sum = r + g + b
    #divide for average
    val = sum // 3
    return (val, val, val)

#second greyscale that uses weighted average to help with the fact that the human eye sees R G B with different intensities
def weighted_greyscale(r, g, b):
    #add up weighted the numbers
    grey = int(0.3 * r + 0.59 * g + 0.11 * b)
    return (grey, grey, grey)

def weird_effect(r, g, b):
    '''
    Weird effect that checks if a red pixel is odd. if it is, block color
    :param r:
    :param g:
    :param b:
    :return:
    '''
    if r % 2 == 0:
        return color.white
    else:
        #add
        return color.black

#exercise 23
def key_red(r,g , b):
    '''
    If both the green and blue values are less than 100, return the original color. Otherwise, return the grayscale color for this pixel
    :param r:red values
    :param g: green values
    :param b:blue values
    :return: color tuple 
    '''
    #loop to check if g and b are less than 100
    if g < 100 and b < 100:
        #return the actual values
        return (r, g, b)
    #if anything else
    else:
        #return the greyscale
        return greyscale(r, g, b)

pygame.init()

#load our image file
#create a pygame surface object with all of the img pixel info
image = pygame.image.load("hidden_message.png")
width = image.get_width()
height = image.get_height()

#make a win that is the same size as the image

win = pygame.display.set_mode((width, height))

#go back and make sure pygame process any alpha transparency in the image
image = image.convert_alpha()

#display image on window
win.blit(image, (0, 0))

pygame.display.update()
pygame_helper.wait_for_click()

#loop through all of the pixels in img and change their values
for y in range(height):
    for x in range(width):
        #x,y will be one particular pixel in the image
        #access the RGB color from this pixel
        # a is just the transpancy
        (r, g, b, a) = image.get_at((x,y))
        #change rgb values
        (r1, g1, b1) = weird_effect(r, g, b)
        #update the pixel in the image
        image.set_at((x,y), (r1, g1, b1))

#reblit
win.blit(image, (0,0))
pygame.display.update()
pygame_helper.wait_for_click()