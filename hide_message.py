#hide message in a photo using steganography
import color
import pygame

pygame.init()

#make a window that we never use so that the colors are read coreectly by pygame
win = pygame.display.set_mode((1,1))

#load image where will hide message
image = pygame.image.load("bug.jpg").convert_alpha()

#step 1
#make all pixels have an even red val
for y in range(image.get_height()):
    for x in range(image.get_width()):
        (r, g, b, a) = image.get_at((x,y))
        if r % 2 != 0:
            #red is currently odd, we need to make it even
            r -= 1
        image.set_at((x,y), (r,g,b))
#all of the reds in the image are even!

#Create some text to hide in the image
#create a pygame font object that we can use
font = pygame.font.SysFont("Veranda", 60)

#create new surface containing our text info
#False turns off anti-aliasing (not going to smooth any corners of the text
#True makes for smoother text on screen
msg = font.render("GO TO PRACTICE !!", False, color.black)

#Loop over the image and the text, anywhere the text is black, make the red pixel in the image odd
for y in range(msg.get_height()):
    for x in range(msg.get_width()):
        (r, g, b, _) = msg.get_at((x,y))


        if (r, g, b) == color.black:
            (ir, ig, ib, ia) = image.get_at((x,y))
            image.set_at((x,y), (ir + 1, ig, ib))



#save image back to a file

pygame.image.save(image, "hidden_message.png")
print("done")