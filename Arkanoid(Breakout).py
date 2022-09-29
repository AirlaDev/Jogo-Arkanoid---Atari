import pygame
from pygame.locals import *
import sys
from pygame.mixer import Sound


AMARELO = (255,255,13)
VERMELHO = (123,15,31)
BRANCO = (255,255,255)
VERDE = (0,255,0)

class JogoBreakout:
    def __init__(jogo):

        jogo.tela = pygame.display.set_mode((800, 600)) #especifica o tamanho da janela
        pygame.display.set_caption("BREAKOUT-ATARI") #coloca um título para a janela
        jogo.blocos = []
        jogo.mouse = [[pygame.Rect(300, 500, 20, 10), 120], #cria o jogador (retângulo)
                [pygame.Rect(320, 500, 20, 10),100],
                [pygame.Rect(340, 500, 20, 10),80],
                [pygame.Rect(360, 500, 20, 10),45],
        ]
        jogo.bola = pygame.Rect(300, 490, 10, 10) #cria a bola do jogo e a posição de partida
        jogo.direcao = -1
        jogo.ydirecao = -1
        jogo.angulo = 80
        jogo.velocidades = {
            120:(-10, -3),
            100:(-10, -8),
            80:(10, -8),
            45:(10, -3),
        }
        jogo.troca = {
            120:45,
            45:120,
            100:80,
            80:100,
        }
        pygame.font.init()
        jogo.font = pygame.font.SysFont("Algerian", 25) #Seleciona uma fonte para usar, tamannho, negrito, italico #fonte da pontuação ('Calibri', 25, True, False)
        jogo.score = 0

        pygame.mixer.init() #inicia o módulo para tocar a musica do jogo
        pygame.mixer.music.load('audio.ogg')
        pygame.mixer.music.play()

    def main(jogo):

        pontos = pygame.time.Clock() #Criamos um objeto Time "clock" este objeto serve para controlarmos o fps do nosso jogo
        jogo.criarBlocos()

        while True:

            pontos.tick(40) #retorna o tempo desde a ultima chamada desse método (também controla a velocidade da bola)
            # O for vai especificar o fechamento da janela:
            for event in pygame.event.get():
                # condição para quando apertar o "x" da janela
                if event.type == pygame.QUIT:
                    sys.exit()
                # condição para quando apertar a tecla "ESC"
                elif event.type == pygame.KEYDOWN:
                      sys.exit()

            #for que especifica as cores do jogo:
            for bloco in jogo.blocos:
                pygame.draw.rect(jogo.tela, AMARELO , bloco) #cor dos blocos(amarelo) (tela, cor, [55, 500, 10, 5])
            for mouse in jogo.mouse:
                pygame.draw.rect(jogo.tela, VERMELHO, mouse[0]) #cor do jogador(mouse)(VERMELHO)
            pygame.draw.rect(jogo.tela, BRANCO, jogo.bola) #cor da bola(branco)
            jogo.tela.blit(jogo.font.render("Placar : " + str(jogo.score), -1, VERDE), (600, 550)) #cor e posição da pontuação /  Coloca o placar na tela

            pygame.display.update()
            jogo.tela.fill((0, 0, 0))
            jogo.atualizaMouse()
            jogo.atualizaBola()


    #função que cria os blocos:
    def criarBlocos(jogo):
        jogo.blocos = []
        y = 50 #posição dos blocos no sentido vertical na tela (cima/baixo)

        #for que cria os blocos 20x20:
        for i in range(20):
            x = 50 #posição dos blocos no sentido horizontal na tela (direita/esquerda)
            for j in range(20):
                bloco = pygame.Rect(x, y, 25, 10) #especifica as dimensões dos blocos
                jogo.blocos.append(bloco)
                x += 35
            y += 12

    def atualizaBola(jogo):
        for k in range(2):
            velocidade = jogo.velocidades[jogo.angulo]
            xmovimento = True

            # if para verificar colisão da bola na parede vertical
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
                jogo.criarBlocos() #atualiza os blocos
                restart = pygame.mixer.Sound("fim.wav")
                restart.play()
                restart.set_volume(0.8)
                jogo.score = 0 #se a bola atingir o fundo da tela reseta o placar
                jogo.bola.x = jogo.mouse[1][0].x #aponta a bola para o jogador
                jogo.bola.y = 490 #atualiza a bola para posição inicial (em cima do jogador)
                jogo.ydirecao = jogo.direcao = -1 #se a bola atingir o topo da tela, inverte a posicao vertical

            # condição que checa se a bola colidiu com o jogador, se sim, inverte a direção vertical da bola:
            for mouse in jogo.mouse:
                if mouse[0].colliderect(jogo.bola):
                    jogo.angulo = mouse[1]
                    jogo.direcao = -1
                    jogo.ydirecao = -1
                    break
    #atualiza a posição do jogador:
    def atualizaMouse(jogo):
        pos = pygame.mouse.get_pos() #retorna uma tupla referente a posição
        on = 0
        for posicao in jogo.mouse:
            posicao[0].x = pos[0] + 20 * on
            on += 1


if __name__ == "__main__":
    JogoBreakout().main()