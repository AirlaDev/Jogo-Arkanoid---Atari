import pygame
from pygame.locals import *
from sys import exit

import os

width, height = 640, 480

pygame.init()
screen = pygame.display.set_mode((width,height), 0, 32)
pygame.display.set_caption("Hello World")

image = pygame.image.load("images" + os.sep + "imagem.png").convert()

img_width, img_height = image.get_size()

x, y = 0,0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(image, (x, y))

    pygame.display.flip() # update()
