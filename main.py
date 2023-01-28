#setting everything up
import pygame
import time
import random
from player import *
from background import *
from NPCs import *
from Dialouge import *
from enemies import *
# pygame.init starts the code
pygame.init()
# create time
clock = pygame.time.Clock()
# main fonts
mainfont = pygame.font.Font(None, 35)
NPCfont = pygame.font.Font(None, 25)
# screen setup
screen = pygame.display.set_mode((1000, 500))
#cant see outside map
def NoFurtherThanBorders():
    global BGX,BGY
    if BGX < -1000:
        BGX = -1000
        PlayerObject.PhysCanMove = True
        #PlayerObject.XSpeed = -5
    if BGX > -5:
        BGX = -5
        PlayerObject.PhysCanMove = True
        #PlayerObject.XSpeed = 5
    if BGY < -500:
        BGY = -500
        PlayerObject.PhysCanMove = True
        #PlayerObject.YSpeed = 5
    if BGY > -5:
        BGY = -5
        PlayerObject.PhysCanMove = True
        #PlayerObject.YSpeed = -5
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
    PlayerObject.PhysMove()
    BGX += BGXSpeed
    BGY += BGYSpeed
    NPCGroup.draw(screen)
    PlayerList.draw(screen)
    EnemiesGroup.update(BGX,BGY)
    EnemiesGroup.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if PlayerObject.rect.x >= 500:
                    PlayerObject.rect.x = 500
                    BGXSpeed = -5
                    PlayerObject.CurrentlyMoving = True

                    if PlayerObject.Direction != "Right":
                        PlayerObject.FlipPlayer()
                    PlayerObject.Direction = "Right"
                #else:
                    #PlayerObject.XSpeed = 5
            if event.key == pygame.K_a:
                if PlayerObject.rect.x <= 500:
                    PlayerObject.rect.x = 500
                    BGXSpeed = 5
                    PlayerObject.CurrentlyMoving = True
                    if PlayerObject.Direction != "Left":
                        PlayerObject.FlipPlayer()
                    PlayerObject.Direction = "Left"
                #else:
                    #PlayerObject.XSpeed = -5
            if event.key == pygame.K_w:
                if PlayerObject.rect.y <= 250:
                    PlayerObject.rect.y = 250
                    BGYSpeed = 5
                    PlayerObject.CurrentlyMoving = True
                    PlayerObject.Direction = "Up"
                    if PlayerObject.Direction != "Up":
                        PlayerObject.FlipPlayer("Up")
                #else:
                    #PlayerObject.YSpeed = -5

            if event.key == pygame.K_s:
                if PlayerObject.rect.y >= 250:
                    PlayerObject.rect.y = 250
                    BGYSpeed = -5
                    PlayerObject.CurrentlyMoving = True
                    PlayerObject.Direction = "Down"
                    if PlayerObject.Direction != "Down":
                        PlayerObject.FlipPlayer("Down")
                #else:
                    #PlayerObject.YSpeed = 5
            if event.key == pygame.K_e:
                for i in range(len(NPCGroup.sprites())):
                    CurrentNPC = NPCGroup.sprites()[i]
                    if PlayerObject.rect.colliderect(CurrentNPC):
                        Conversation(CurrentNPC, screen, GrassAndDirtBG1, BGX, BGY, PlayerList,NPCGroup)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                BGXSpeed = 0
                PlayerObject.XSpeed = 0
                PlayerObject.CurrentlyMoving = False
            if event.key == pygame.K_a:
                BGXSpeed = 0
                PlayerObject.XSpeed = 0
                PlayerObject.CurrentlyMoving = False
            if event.key == pygame.K_w:
                BGYSpeed = 0
                PlayerObject.YSpeed = 0
                PlayerObject.CurrentlyMoving = False
            if event.key == pygame.K_s:
                BGYSpeed = 0
                PlayerObject.YSpeed = 0
                PlayerObject.CurrentlyMoving = False
    for i in range(len(NPCGroup.sprites())):
        CurrentNPC = NPCGroup.sprites()[i]
        if PlayerObject.rect.colliderect(CurrentNPC):
            text = NPCfont.render("Press E to interact", True, (0, 0, 0))
            textx = CurrentNPC.rect.x
            texty = CurrentNPC.rect.y
            screen.blit(text, (textx - 35, texty - 10))
    PlayerList.update()
    NPCGroup.update(BGX, BGY)
    CurrentTime = (pygame.time.get_ticks() / 1000)
    clock.tick(60)
    text = NPCfont.render("Enemy X:" + str(GlitchedSlime1.x), True, (0,0,0))
    screen.blit(text, (20, 20))
    text = NPCfont.render("Enemy Y:" + str(GlitchedSlime1.y), True, (0,0,0))
    screen.blit(text, (20, 40))
    text = NPCfont.render("Player X:" + str(BGX), True, (0,0,0))
    screen.blit(text, (20, 60))
    text = NPCfont.render("Player Y:" + str(BGY), True, (0,0,0))
    screen.blit(text, (20, 80))
    pygame.display.flip()
