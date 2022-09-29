import pygame
from pygame.locals import *
from sys import exit

import os
import bouncer

import pygame
from pygame.locals import *
import sys
from pygame.mixer import Sound


AMARELO = (255,255,13)
VERMELHO = (123,15,31)
BRANCO = (255,255,255)
VERDE = (0,255,0)

screen_width, screen_height = 800, 600

pygame.init()
pygame.display.set_caption("BREAKOUT-ATARI")
screen = pygame.display.set_mode((screen_width,screen_height), 0, 32)

new_game_buttons = [pygame.image.load("images" + os.sep + "novo_jogo" + str(i+1) + ".png").convert()\
for i in range(3)]
new_game_button = new_game_buttons[0]
new_game_size = new_game_button.get_size()
new_game_pos = (screen_width/2 - new_game_size[0]/2, screen_height/3 - new_game_size[1]/2)

exit_buttons = [pygame.image.load("images" + os.sep + "sair" + str(i+1) + ".png").convert()\
                for i in range(3)]
exit_button = exit_buttons[0]
exit_size = exit_button.get_size()
exit_pos = (screen_width/2 - exit_size[0]/2, 2*screen_height/3 - exit_size[1]/2)


background = pygame.image.load("images" + os.sep + "atari.jpg").convert()

pressed = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    mouse_pos = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()

    # Novo Jogo
    if new_game_pos[0] <= mouse_pos[0] <= new_game_pos[0] + new_game_size[0]\
       and new_game_pos[1] <= mouse_pos[1] <= new_game_pos[1] + new_game_size[1]:

        new_game_button = new_game_buttons[1]

        if mouse_press[0]:
            new_game_button = new_game_buttons[2]
            pressed = True


            class JogoBreakout:
                def __init__(jogo):

                    jogo.tela = pygame.display.set_mode((800, 600))  # especifica o tamanho da janela
                    pygame.display.set_caption("BREAKOUT-ATARI")  # coloca um título para a janela

                    jogo.mouse = [[pygame.Rect(300, 500, 20, 10), 120],  # cria o jogador (retângulo)
                                  [pygame.Rect(320, 500, 20, 10), 100],
                                  [pygame.Rect(340, 500, 20, 10), 80],
                                  [pygame.Rect(360, 500, 20, 10), 45],
                                  ]
                    jogo.bola = pygame.Rect(300, 490, 10, 10)  # cria a bola do jogo e a posição de partida
                    jogo.direcao = -1
                    jogo.ydirecao = -1
                    jogo.angulo = 80
                    jogo.velocidades = {120: (-10, -3), 100: (-10, -8), 80: (10, -8), 45: (10, -3), }
                    jogo.troca = {120: 45, 45: 120, 100: 80, 80: 100, }
                    pygame.font.init()
                    jogo.font = pygame.font.SysFont("Algerian",
                                                    25)  # Seleciona uma fonte para usar, tamannho, negrito, italico #fonte da pontuação ('Calibri', 25, True, False)
                    jogo.score = 0

                    pygame.mixer.init()  # inicia o módulo para tocar a musica do jogo
                    pygame.mixer.music.load('audio.ogg')
                    pygame.mixer.music.play()

                def main(jogo):

                    pontos = pygame.time.Clock()  # Criamos um objeto Time "clock" este objeto serve para controlarmos o fps do jogo
                    jogo.criarBlocos()

                    while True:

                        pontos.tick(40)  # controla a velocidade da bola
                        # O for vai especificar o fechamento da janela:
                        for event in pygame.event.get():
                            # condição para quando apertar o "x" da janela
                            if event.type == pygame.QUIT:
                                sys.exit()
                            # condição para quando apertar a tecla "ESC"
                            elif event.type == pygame.KEYDOWN:
                                sys.exit()

                        # especifica as cores do jogo:
                        for bloco in jogo.blocos:
                            pygame.draw.rect(jogo.tela, AMARELO,
                                             bloco)  # cor dos blocos(amarelo) (tela, cor, [55, 500, 10, 5])
                        for mouse in jogo.mouse:
                            pygame.draw.rect(jogo.tela, VERMELHO, mouse[0])  # cor do jogador(mouse)(VERMELHO)
                        pygame.draw.rect(jogo.tela, BRANCO, jogo.bola)  # cor da bola(branco)
                        jogo.tela.blit(jogo.font.render("Placar : " + str(jogo.score), -1, VERDE),
                                       (600, 550))  # cor e posição da pontuação /  Coloca o placar na tela

                        pygame.display.update()
                        jogo.tela.fill((0, 0, 0))
                        jogo.atualizaMouse()
                        jogo.atualizaBola()

                # cria os blocos:
                def criarBlocos(jogo):
                    jogo.blocos = []
                    y = 50  # posição dos blocos no sentido vertical na tela (cima/baixo)

                    # cria os blocos 20x20:
                    for i in range(20):
                        x = 50  # posição dos blocos no sentido horizontal na tela (direita/esquerda)
                        for j in range(20):
                            bloco = pygame.Rect(x, y, 25, 10)  # especifica as dimensões dos blocos
                            jogo.blocos.append(bloco)
                            x += 35
                        y += 12

                def atualizaBola(jogo):
                    for k in range(2):
                        velocidade = jogo.velocidades[jogo.angulo]
                        xmovimento = True

                        # verificar colisão da bola na parede vertical
                        if k:
                            jogo.bola.x += velocidade[0] * jogo.direcao

                        else:
                            jogo.bola.y += velocidade[1] * jogo.direcao * jogo.ydirecao
                            xmovimento = False

                        # verifica se a bola colide com a parede vertical:

                        if jogo.bola.x <= 0 or jogo.bola.x >= 800:
                            jogo.angulo = jogo.troca[jogo.angulo]
                            if jogo.bola.x <= 0:
                                jogo.bola.x = 1
                            else:
                                jogo.bola.x = 799

                        # se a bola atingir a lateral da tela, inverte a posicao horizontal:
                        if jogo.bola.y <= 0:
                            jogo.bola.y = 1
                            jogo.ydirecao *= -1

                        # if para verificar colisão da bola com os blocos:
                        verificar = jogo.bola.collidelist(jogo.blocos)
                        if verificar != -1:
                            bloco = jogo.blocos.pop(verificar)

                            colisao = pygame.mixer.Sound("som.wav")
                            colisao.play()
                            colisao.set_volume(0.8)

                            if xmovimento:
                                jogo.direcao *= -1
                            jogo.ydirecao *= -1
                            jogo.score += 1  # se a bola colidir com os blocos, incrementa o placar

                        # condição que verifica se a bola colide com o fundo e topo da tela:
                        if jogo.bola.y > 600:
                            jogo.criarBlocos()  # atualiza os blocos
                            restart = pygame.mixer.Sound("fim.wav")
                            restart.play()
                            restart.set_volume(0.8)
                            jogo.score = 0  # se a bola atingir o fundo da tela reseta o placar
                            jogo.bola.x = jogo.mouse[1][0].x  # aponta a bola para o jogador
                            jogo.bola.y = 490  # atualiza a bola para posição inicial (em cima do jogador)
                            jogo.ydirecao = jogo.direcao = -1  # se a bola atingir o topo da tela, inverte a posicao vertical

                        # condição que checa se a bola colidiu com o jogador, se sim, inverte a direção vertical da bola:
                        for mouse in jogo.mouse:
                            if mouse[0].colliderect(jogo.bola):
                                jogo.angulo = mouse[1]
                                jogo.direcao = -1
                                jogo.ydirecao = -1
                                break

                # atualiza a posição do jogador:
                def atualizaMouse(jogo):
                    pos = pygame.mouse.get_pos()  # referente a posição do mouse
                    on = 0
                    # certifica o movimento horizontal do mouse e o estilo do retangulo
                    for posicao in jogo.mouse:
                        posicao[0].x = pos[0] + 15 * on
                        on += 1


            if __name__ == "__main__":
                JogoBreakout().main()


    else: new_game_button = new_game_buttons[0]

    # Sair
    if exit_pos[0] <= mouse_pos[0] <= exit_pos[0] + exit_size[0]\
       and exit_pos[1] <= mouse_pos[1] <= exit_pos[1] + exit_size[1]:

        exit_button = exit_buttons[1]

        if mouse_press[0]:
            exit_button = exit_buttons[2]
            pressed = True

        if pressed and not mouse_press[0]:
            exit_button = exit_buttons[1]
            exit()

    else: exit_button = exit_buttons[0]

    if not mouse_press[0]:
        pressed = False

    screen.blit(background, (0,0))

    screen.blit(exit_button, exit_pos)
    screen.blit(new_game_button, new_game_pos)

    pygame.display.update()


