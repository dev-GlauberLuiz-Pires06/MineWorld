#!/usr/bin/python3

import pygame
from pygame.locals import *

from auxilio import *
from seres.personagem import *
from objetos.slots import *

from classMapa import *

janela = pygame.display.set_mode((1366, 786))
pygame.display.set_caption("Mine World")

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

mapa = Mapa()

personagem = Persona(janela, mapa, 0, 0)

lista = []

for a in range(-1, 2):
    for b in range(-1, 2):
        lista.append(Slots(janela, mapa, a, b))

print(lista)

janela_aberta = True

while janela_aberta:

    pygame.time.delay(100)

    janela.fill(BLACK)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            janela_aberta = False

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

    if janela_aberta == False:
        pass

    for a in lista:
        a.atualizar()

    personagem.atualizar(teclas)

    pygame.display.update()
