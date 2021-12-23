import pygame
from pygame.draw import *
from auxilio import *

class Chao:
    def __init__(self, janela, mapa, x, y):
        self.janela = janela
        self.mapa = mapa

        self.posX = x
        self.posY = y
        self.tamX = 32
        self.tamY = 32

    def atualizar(self):
        rect(self.janela, GREEN, ((self.posX + self.mapa.posX), (self.posY + self.mapa.posY), self.tamX, self.tamY))
        rect(self.janela, RED, ((self.posX + self.mapa.posX), (self.posY + self.mapa.posY), self.tamX, self.tamY), 2)
