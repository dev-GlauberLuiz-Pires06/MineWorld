import pygame
from auxilio import *

class Objeto:
    def __init__(self, janela, mapa, x, y):
        self.janela = janela
        self.mapa = mapa

        self.posX = x * 32
        self.posY = y * 32
        self.tamX = 32
        self.tamY = 32

    def atualizar(self, x, y):
        pygame.draw.rect(self.janela, RED, ((self.posX + self.mapa.posX + x), (self.posY + self.mapa.posY + y), self.tamX, self.tamY), 1)
