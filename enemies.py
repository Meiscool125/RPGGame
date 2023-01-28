# SPRITE OG SIZE 50x50
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
# lists/groups
SlimeGlitchedAnimationSpriteSheetList = []
EnemyGroup = pygame.sprite.Group()
# ERROR TEXTURE
PINKANDBLACKERRORTEXTURE = pygame.image.load("assets/PinkAndBlackErrorTexture.jpeg")
PINKANDBLACKERRORTEXTURE = pygame.transform.scale(PINKANDBLACKERRORTEXTURE, (20, 20))
# sprite group
EnemiesGroup = pygame.sprite.Group()
# NPC Sprites class
SlimeGlitchedSpriteSheet = pygame.image.load("assets/Slime Glitched SpriteSheet.png")
# create individual frames
for i in range(3):
    Frame = pygame.Surface.subsurface(SlimeGlitchedSpriteSheet, (i * 50, 0, 50, 50))
    SlimeGlitchedAnimationSpriteSheetList.append(Frame)
GlitchedSlimeDefaultSprite = SlimeGlitchedAnimationSpriteSheetList[0]
GlitchedSlimeGettingReadyToJumpSquished = SlimeGlitchedAnimationSpriteSheetList[1]
GlitchedSlimeInMidair = SlimeGlitchedAnimationSpriteSheetList[2]

class Enemies(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, EnemyType):
        super().__init__()
        self.image = PINKANDBLACKERRORTEXTURE
        self.image = pygame.transform.scale(self.image, (width, height))
        if EnemyType == "GlitchedSlime":
            self.image = GlitchedSlimeDefaultSprite
            self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.x = x
        self.xOrgin = x
        self.y = y
        self.yOrigin = y
        self.EnemyState = "Chilling"
        self.movetimer = pygame.time.get_ticks()
    def CalculateXMovement(self, direction):
        # -x ^ 2 + 3x + 10
        self.startx = self.x
        self.starty = self.y
        if direction == "Right":
            for i in range(5):
                self.startx = self.x
                self.starty = self.y
                self.x += 5
                self.y = (-((self.x - self.startx) ** 2) + (3 * (self.x-self.startx)) + 10) + self.starty
        if direction == "Left":
            for i in range(5):
                self.startx = self.x
                self.starty = self.y
                self.x += 5
                self.y = (-((self.x-self.startx) ** 2) + (-3 * (self.x-self.startx)) + 10) + self.starty
            #print(self.x)
    def update(self, BGX, BGY):
        self.rect.x = self.x + BGX
        self.rect.y = self.y + BGY
        if self.EnemyState == "Chilling":
            if pygame.time.get_ticks() - self.movetimer > 1000:
                self.ChooseMovement()
                self.movetimer = pygame.time.get_ticks()
                #print("ohio")
    def ChooseMovement(self):
        if random.randint(1, 1) == 1: # will we move? 1 means yes
            if random.randint(2, 2) == 1: # will we move up/down or left/right (x or y)? 1 is up/down vice versa
                if random.randint(1,2) == 1: # 1 is moving down 2 is moving up
                    pass
                else:
                    pass
            else:
                if random.randint(1,2) == 1: # 1 is moving left 2 is moving right
                    self.CalculateXMovement("Left")
                else:
                    self.CalculateXMovement("Right")

GlitchedSlime1 = Enemies(700, 500, 50, 50, "GlitchedSlime")
EnemiesGroup.add(GlitchedSlime1)