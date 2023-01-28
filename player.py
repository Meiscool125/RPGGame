# SPRITE OG SIZE 45x75
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
# lists
RightWalkAnimationList = []
#load image
PlayerAnimationWalkingRightSpriteSheet = pygame.image.load("assets/WalkingRightAnimationFrameList.png")
for i in range(10):
    Frame = pygame.Surface.subsurface(PlayerAnimationWalkingRightSpriteSheet, (i * 45, 0, 45, 75))
    RightWalkAnimationList.append(Frame)
#player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.RightWalkAnimationList = RightWalkAnimationList
        self.AnimationIndex = 0
        self.TimeSinceLastFrame = pygame.time.get_ticks() / 1000
        self.image = self.RightWalkAnimationList[self.AnimationIndex]
        self.rect = self.image.get_rect()
        self.PhysCanMove = False
        self.rect.x = x
        self.rect.y = y
        self.XSpeed = 0
        self.YSpeed = 0
        self.CurrentlyMoving = False
        self.Direction = "Right"
        self.AtBorderEdge = False
    def UpdateAnimations(self, CurrentTime):
        if CurrentTime - self.TimeSinceLastFrame > 0.3:
            self.AnimationIndex += 1
            if self.AnimationIndex > 9:
                self.AnimationIndex = 0
            self.TimeSinceLastFrame = pygame.time.get_ticks() / 1000
    def update(self):
        if self.CurrentlyMoving and self.AtBorderEdge == False:
            self.image = self.RightWalkAnimationList[self.AnimationIndex]

            if (pygame.time.get_ticks() / 1000) - self.TimeSinceLastFrame > 0.1:
                self.AnimationIndex += 1
                if self.AnimationIndex > 9:
                    self.AnimationIndex = 0
                self.TimeSinceLastFrame = pygame.time.get_ticks() / 1000
    def FlipPlayer(self):

        self.image = pygame.transform.flip(self.image, True, False)

    def PhysMove(self):
        self.rect.x += self.XSpeed
        self.rect.y += self.YSpeed
        #if self.rect.x > 500:
            #self.XSpeed = 0
        #if self.rect.x < -1000:
            #self.XSpeed = 0


