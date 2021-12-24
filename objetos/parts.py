import pygame
from auxilio import *
from objetos.obj import *

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

        # definir os objetos da part
        for a in range(0, 40):
            for b in range(0, 40):
                self.lista.append(Objeto(self.janela, self.mapa, a, b))

    def atualizar(self):
        for a in self.lista:
            a.atualizar(self.posX, self.posY)
    def salvar(self):
        pass
