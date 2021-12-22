#!/usr/bin/python3

import pygame
from pygame.locals import *

from auxilio import *

janela = pygame.display.set_mode((1366, 786))
pygame.display.set_caption("Mine World")

janela_aberta = True

while janela_aberta:

    pygame.time.delay(100)

    janela.fill(BLUE)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            janela_aberta = False

        if evento.type == pygame.KEYDOWN:
            pass

        if evento.type == pygame.KEYUP:
            pass

    if janela_aberta == False:
        pass

    pygame.display.update()
