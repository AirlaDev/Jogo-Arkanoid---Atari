import pygame
from pygame.locals import *
from sys import exit

import os

width, height = 640, 480

pygame.init()
screen = pygame.display.set_mode((width,height), 0, 32)
pygame.display.set_caption("Hello World")

verde = (0, 255, 0)
font = pygame.font.SysFont("courrier new", 60, bold = False)	
image = font.render("Hello World", True, verde)

img_width, img_height = image.get_size()

x, y = width/2 - img_width/2, height/2 - img_height/2;

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(image, (x,y))

    pygame.display.flip() # update()
