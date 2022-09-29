import pygame
from pygame.locals import *
from sys import exit

import os

width, height = 640, 480

pygame.init()
screen = pygame.display.set_mode((width,height), 0, 32)
pygame.display.set_caption("Hello World")

# Carrega algumas imagens para o jogo.
image = pygame.image.load("images" + os.sep + "hello_world.png").convert()
img_pedra = pygame.image.load("images" + os.sep + "pedra.gif").convert()
img_garrafa = pygame.image.load("images" + os.sep + "objetos" + os.sep + "garrafa.png").convert_alpha()

img_width, img_height = image.get_size()

x, y = width/2 - img_width/2, height/2 - img_height/2
x_pedra, y_pedra = 20, height/2 - img_pedra.get_height()/2
x_garrafa, y_garrafa = 400, height/2 - img_garrafa.get_height()/2

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(image, (x, y))
    screen.blit(img_pedra, (x_pedra, y_pedra))
    screen.blit(img_garrafa, (x_garrafa, y_garrafa))

    pygame.display.flip() # update()
