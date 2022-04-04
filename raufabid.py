import sys
import os
import pygame 
import random 
import math

    
pygame.init()
pygame.display.set_caption("Abid Amculleey rauf")
pygame.font.init()
random.seed()
SPEED = 0.36
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE
SEPARATION = 10
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP":1,"DOWN":2,"LEFT":3,"RIGHT":4}
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.HWSURFACE)
background_color = pygame.Color(74,74,74)
black = pygame.Color(0,0,0)
class gameframe():

    def checkCollision(posA,As,posB,Bs):
        if(posA.x   < posB.x+Bs and posA.x+As > posB.x and posA.y < posB.y + Bs and posA.y+As > posB.y):
            return True
        return False

    def checkLimits(entity):
            if(entity.x > SCREEN_WIDTH):
                entity.x = SNAKE_SIZE
            if(entity.x < 0):
                entity.x = SCREEN_WIDTH - SNAKE_SIZE
            if(entity.y > SCREEN_HEIGHT):
                entity.y = SNAKE_SIZE
            if(entity.y < 0):
                entity.y = SCREEN_HEIGHT - SNAKE_SIZE
    def checkLimits(entity):
        if(entity.x > SCREEN_WIDTH):
            entity.x = SNAKE_SIZE
        if(entity.x < 0):
            entity.x = SCREEN_WIDTH - SNAKE_SIZE
        if(entity.y > SCREEN_HEIGHT):
            entity.y = SNAKE_SIZE
        if(entity.y < 0):
            entity.y = SCREEN_HEIGHT - SNAKE_SIZE
    def getKey():
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        return KEY["UP"]
                    elif event.key == pygame.K_DOWN:
                        return KEY["DOWN"]
                    elif event.key == pygame.K_LEFT:
                        return KEY["LEFT"]
                    elif event.key == pygame.K_RIGHT:
                        return KEY["RIGHT"]
                    elif event.key == pygame.K_ESCAPE:
                        return "exit"
                    elif event.key == pygame.K_y:
                        return "yes"
                    elif event.key == pygame.K_n:
                        return "no"
                if event.type == pygame.QUIT:
                    sys.exit() 
    def endGame():
        message = game_over_font.render("Oyundan sikdirdin",1,pygame.Color("blue"))
        message_play_again = play_again_font.render("Oynuyax? Y/N",1,pygame.Color("red"))
        screen.blit(message,(320,240))
        screen.blit(message_play_again,(320+12,240+40))

        pygame.display.flip()
        pygame.display.update()
        
        myKey = getKey()
        while(myKey != "exit"):
            if(myKey == "yes"):
                main()
            elif(myKey == "no"):
                break
            myKey = getKey()
            gameClock.tick(FPS)
        sys.exit()

    def drawScore(score):
        score_numb = score_numb_font.render(str(score),1,pygame.Color("red"))
        screen.blit(score_msg, (SCREEN_WIDTH-score_msg_size[0]-60,10) )
        screen.blit(score_numb,(SCREEN_WIDTH - 45,14))
        
    def drawGameTime(gameTime):
        game_time = score_font.render("Time:",1,pygame.Color("green"))
        game_time_numb = score_numb_font.render(str(gameTime/1000),1,pygame.Color("red"))
        screen.blit(game_time,(30,10))
        screen.blit(game_time_numb,(105,14))
        
    def exitScreen():
        pass
if __name__=="__name__":
        gameframe();                        
