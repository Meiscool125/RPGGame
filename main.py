#setting everything up
import pygame
import time
import random
from player import *
from background import *
# pygame.init starts the code
pygame.init()
# create time
clock = pygame.time.Clock()
# main fonts
mainfont = pygame.font.Font(None, 35)
# screen setup
screen = pygame.display.set_mode((1000, 500))
#cant see outside map
def NoFurtherThanBorders():
    global BGX,BGY
    if BGX < -1000:
        BGX = -1000
    if BGX > -5:
        BGX = -5
    if BGY < -500:
        BGY = -500
    if BGY > -5:
        BGY = -5
# make player object
PlayerObject = Player(500, 250)
# player list
PlayerList = pygame.sprite.Group()
PlayerList.add(PlayerObject)
# always do this
CurrentlyRunning = True
while CurrentlyRunning:
    screen.fill((0,0,0))
    screen.blit(GrassAndDirtBG1, (BGX, BGY))
    NoFurtherThanBorders()
    BGX += BGXSpeed
    BGY += BGYSpeed
    PlayerList.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                BGXSpeed = -5
            if event.key == pygame.K_a:
                BGXSpeed = 5
            if event.key == pygame.K_w:
                BGYSpeed = 5
            if event.key == pygame.K_s:
                BGYSpeed = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                BGXSpeed = 0
            if event.key == pygame.K_a:
                BGXSpeed = 0
            if event.key == pygame.K_w:
                BGYSpeed = 0
            if event.key == pygame.K_s:
                BGYSpeed = 0
    CurrentTime = (pygame.time.get_ticks() / 1000)
    clock.tick(60)
    pygame.display.flip()
