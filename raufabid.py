import sys
import os
import pygame 
import random 
import math

from sympy import true
    
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

if __name__=="__name__":
        gameframe();                        