import pygame
from auxilio import *

class Parts: # parte do mapa
    def __init__(self, janela, mapa, x, y):
        self.janela = janela
        self.mapa = mapa # ponto de referencia espacial

        # cordenadas
        self.locX = x
        self.locY = y

        # posição da part
        self.posX = posM(x)
        self.posY = posM(y)

        self.lista = [] # lista de objetos da part

    def atualizar(self):
        pygame.draw.rect(self.janela, RED, ((self.posX + self.mapa.posX), (self.posY + self.mapa.posY), pos(40), pos(40)), 1)

    def salvar(self):
        pass
