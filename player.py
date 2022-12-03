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
        self.TimeSinceLastFrame = 0
        self.image = self.RightWalkAnimationList[self.AnimationIndex]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def UpdateAnimations(self):
        if self.TimeSinceLastFrame > 0.3:
            self.AnimationIndex += 1
            self.image = self.RightWalkAnimationList[self.AnimationIndex]