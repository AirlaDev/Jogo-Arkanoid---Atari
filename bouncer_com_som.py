import pygame
from pygame.locals import *
from sys import exit

import os

screen_width, screen_height = 640, 480

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height), 0, 32)
pygame.display.set_caption("Exemplo 3")

#Carrega os sons
som_colisao = pygame.mixer.Sound("sounds" + os.sep + "tabela.wav")
som_colisao.set_volume(1.0)

# Variaveis da bola
ball_image = pygame.image.load('images' + os.sep + "ball.png").convert()
ball_width, ball_height = ball_image.get_size()
ball_x, ball_y = (screen_width/2 - ball_width/2), ball_height
posicao_inicial = (ball_x, ball_y)
ball_varia_x = 7
ball_varia_y = 7

# Variaveis do bouncer
bouncer_image = pygame.image.load('images' + os.sep + "bouncer.png").convert()
bouncer_width, bouncer_height = bouncer_image.get_size()
bouncer_x, bouncer_y = (screen_width/2 - bouncer_width/2), (screen_height - bouncer_height)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    screen.fill((255, 255, 255))
    
    pressed_keys = pygame.key.get_pressed()

    # Verifica colisao com a tela
    if ball_x <= 0 or ball_x + ball_width >= screen_width:
        ball_varia_x = -ball_varia_x
        som_colisao.play()

    if ball_y <= 0:
        ball_varia_y = -ball_varia_y
        som_colisao.play()

    if ball_y + ball_height >= screen_height:
        ball_x, ball_y = posicao_inicial[0], posicao_inicial[1]

    # Verifica colisao com o bouncer
    if ball_y + ball_height >= bouncer_y:
        if bouncer_x <= ball_x <= bouncer_x + bouncer_width:
            ball_varia_y = -ball_varia_y
            som_colisao.play()
        elif bouncer_x <= ball_x + ball_width <= bouncer_x + bouncer_width:
            ball_varia_y = -ball_varia_y
            som_colisao.play()

    # Movimenta a bola
    ball_x += ball_varia_x
    ball_y += ball_varia_y

    # Movimenta o bouncer
    if pressed_keys[K_LEFT] and bouncer_x > 0:
        bouncer_x -= 5
    if pressed_keys[K_RIGHT] and bouncer_x < screen_height:
        bouncer_x += 5
        
    screen.blit(ball_image, (ball_x, ball_y))
    screen.blit(bouncer_image, (bouncer_x, bouncer_y))

    pygame.display.flip()
