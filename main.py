#!/usr/bin/python3

import pygame
from pygame.locals import *
from personagem import *
from auxilio import *

janela = pygame.display.set_mode((1366, 786))
pygame.display.set_caption("Mine World")

teclas = [
False,    # A                    0
False,    # W                    1
False,    # S                    2
False,    # D                    3
False,    # J                    4
False,    # K                    5
False,    # L                    6
False,    # U                    7
False,    # I                    8
False,    # O                    9
False,    # seta pra cima        10
False,    # seta pra baixo       11
False,    # seta pra direita     12
False,    # seta pra esquerda    13
False     # espaço               14
]

ponto_de_referencia = Ref()
personagem = Personagem(janela, ponto_de_referencia, 0, 0)

rodando = True
while rodando:

    pygame.time.delay(33)

    janela.fill(BLACK)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False

        if evento.type == KEYDOWN:
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
            if evento.key == K_RIGHT:
                teclas[12] = True
            if evento.key == K_LEFT:
                teclas[13] = True
            if evento.key == K_SPACE:
                teclas[14] = True

        if evento.type == KEYUP:
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
            if evento.key == K_RIGHT:
                teclas[12] = False
            if evento.key == K_LEFT:
                teclas[13] = False
            if evento.key == K_SPACE:
                teclas[14] = False

    personagem.atualizar(teclas)

    pygame.display.update()
