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
# fonts
NPCfont = pygame.font.Font(None, 25)
#stuff
def Conversation(NPC, screen, BGImage, BGX, BGY, PlayerGroup, NPCGroup):
    IsTalking = True
    TimesEHasBeenPressedInThisConversation = 0
    while IsTalking == True:
        screen.blit(BGImage, (BGX, BGY))
        NPCGroup.draw(screen)
        PlayerGroup.draw(screen)
        ScreenText = NPCfont.render(NPC.PromptText[TimesEHasBeenPressedInThisConversation], True, (0, 0, 0))
        screen.blit(ScreenText, (50, 400))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    TimesEHasBeenPressedInThisConversation += 1
        if TimesEHasBeenPressedInThisConversation == len(NPC.PromptText):
            IsTalking = False
        pygame.display.flip()
