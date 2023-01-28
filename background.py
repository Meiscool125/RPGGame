#setting everything up
import pygame
import time
import random
# pygame.init starts the code
pygame.init()
# create time
clock = pygame.time.Clock()
# main fonts
mainfont = pygame.font.Font(None, 35)
# background variables
BGX = -50
BGY = -50
BGXSpeed = 0
BGYSpeed = 0
# function
def UpdateBG():
    global BGX, BGY, BGXSpeed, BGYSpeed
    BGX += BGXSpeed
    BGY += BGYSpeed
# make screen
GrassAndDirtBG1 = pygame.image.load('assets/grassImageClear.JPG')
GrassAndDirtBG1 = pygame.transform.scale(GrassAndDirtBG1, (3000, 1500))