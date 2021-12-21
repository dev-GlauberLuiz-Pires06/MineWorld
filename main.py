#!/usr/bin/python3

import pygame
from pygame.locals import *

from auxilio import *
from jogo import *

janela = pygame.display.set_mode((1366, 786))
pygame.display.set_caption("Mine World")

mundo = Jogo(janela)

janela_aberta = True
while janela_aberta:

    pygame.time.delay(100)

    janela.fill(BLACK)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            janela_aberta = False

    if janela_aberta == False:
        pass

    mundo.atualizar()

    pygame.display.update()