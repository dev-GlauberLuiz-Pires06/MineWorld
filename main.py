#!/usr/bin/python3

# bibliotecas
import pygame
from pygame.locals import *

from auxilio import *
from seres.personagem import *
from objetos.parts import *

from classMapa import *
# ==============================================================================
# Carrega o jogo

# tela
janela = pygame.display.set_mode((1366, 786))
pygame.display.set_caption("Mine World")

# mostra quais as teclas precionadas
teclas = [False,        # A                    0
         False,         # W                    1
         False,         # S                    2
         False,         # D                    3
         False,         # J / 1                4
         False,         # K / 2                5
         False,         # L / 3                6
         False,         # U / 4                7
         False,         # I / 5                8
         False,         # O / 6                9
         False,         # seta pra cima        10
         False,         # seta pra baixo       11
         False,         # seta pra esquerda    12
         False]         # seta pra direita     13

mapa = Mapa() # é um ponto de orientação (x, y) para tudo

personagem = Persona(janela, mapa, 0, 0)

lista = [] # lista de pedaços do mapa que formam o mapa

# ==============================================================================
# Mantem a janela aberta

janela_aberta = True

while janela_aberta:

    pygame.time.delay(100)

    janela.fill(GREEN)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            janela_aberta = False

        # verifica as teclas precionadas e as coloca na variavel <teclas>
        if evento.type == pygame.KEYDOWN:
            if evento.key == K_a:
                teclas[0] = True
            if evento.key == K_w:
                teclas[1] = True
            if evento.key == K_s:
                teclas[2] = True
            if evento.key == K_d:
                teclas[3] = True
            if evento.key == K_j:
                teclas[4] = True
            if evento.key == K_k:
                teclas[5] = True
            if evento.key == K_l:
                teclas[6] = True
            if evento.key == K_u:
                teclas[7] = True
            if evento.key == K_i:
                teclas[8] = True
            if evento.key == K_o:
                teclas[9] = True
            if evento.key == K_UP:
                teclas[10] = True
            if evento.key == K_DOWN:
                teclas[11] = True
            if evento.key == K_LEFT:
                teclas[12] = True
            if evento.key == K_RIGHT:
                teclas[13] = True
        if evento.type == pygame.KEYUP:
            if evento.key == K_a:
                teclas[0] = False
            if evento.key == K_w:
                teclas[1] = False
            if evento.key == K_s:
                teclas[2] = False
            if evento.key == K_d:
                teclas[3] = False
            if evento.key == K_j:
                teclas[4] = False
            if evento.key == K_k:
                teclas[5] = False
            if evento.key == K_l:
                teclas[6] = False
            if evento.key == K_u:
                teclas[7] = False
            if evento.key == K_i:
                teclas[8] = False
            if evento.key == K_o:
                teclas[9] = False
            if evento.key == K_UP:
                teclas[10] = False
            if evento.key == K_DOWN:
                teclas[11] = False
            if evento.key == K_LEFT:
                teclas[12] = False
            if evento.key == K_RIGHT:
                teclas[13] = False

    # ==========================================================================
    # Processamento do jogo

    # finaliza e salva as informações
    if janela_aberta == False:
        pass

    # atualiza o mapa parts mais proximas          atualizar somente os proximos
    for a in range(-1, 2):
        for b in range(-1, 2):
            funcionou = False
            for c in lista:
                if c.locX == (a + personagem.locX):
                    if c.locY == (b + personagem.locY):
                        funcionou = True
                        c.atualizar()
            if funcionou == False:
                lista.append(Parts(janela, mapa, (a + personagem.locX), (b + personagem.locY)))

    personagem.atualizar(teclas) # atualiza o personagem principal

    pygame.display.update()
