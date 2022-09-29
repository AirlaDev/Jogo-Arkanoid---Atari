import pygame
from pygame.locals import *
from sys import exit

import os

width, height = 640, 480

pygame.init()
screen = pygame.display.set_mode((width,height), 0, 32)
pygame.display.set_caption("Exemplo 2")

image = pygame.image.load('images' + os.sep + "hello_world.png").convert()

img_width, img_height = image.get_size()

x, y = width/2 - img_width/2, height/2 - img_height/2;

varia_x, varia_y = 1, 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    if x + img_width >= width or x <= 0:
        varia_x = -varia_x

    if y + img_height >= height or y <= 0:
        varia_y = -varia_y

    x += varia_x
    y += varia_y
    
    screen.blit(image, (x, y))

    pygame.display.flip() # update()
