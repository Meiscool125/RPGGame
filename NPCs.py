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
NPCGroup = pygame.sprite.Group()
# NPC Sprites class
class NPCsClass(pygame.sprite.Sprite):
    def __init__(self, x, y, FrameList):
        super().__init__()
        self.FrameList = FrameList
        self.FrameNumber = 0
        self.image = self.FrameList[self.FrameNumber]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.PromptText = []
    def update(self, BGX, BGY):
        self.rect.x = self.x + BGX
        self.rect.y = self.y + BGY
    def AddText(self, text):
        self.PromptText.append(text)

# Balloon NPC info
GlitchedBalloonNPCList = []
GlitchedBalloonNPCSpriteSheet = pygame.image.load("assets/Balloon NPC Glitched State Spritesheet.png")
GlitchedBalloonNPCSpriteSheet = pygame.transform.scale(GlitchedBalloonNPCSpriteSheet, (60 * 2, 85))
for i in range(2):
    Frame = pygame.Surface.subsurface(GlitchedBalloonNPCSpriteSheet, (i * 60, 0, 60, 85))
    GlitchedBalloonNPCList.append(Frame)
GlitchedBalloonNPC = NPCsClass(1500, 750, GlitchedBalloonNPCList)
NPCGroup.add(GlitchedBalloonNPC)
GlitchedBalloonNPC.AddText("Hey there, I'm ! However, when _____ took over, I became corrupted, just like all the others in this game.")


