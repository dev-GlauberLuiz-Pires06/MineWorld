import pygame
from auxilio import *
from objetos.chao import *

class Slots:
    def __init__(self, janela, mapa, x, y):
        self.janela = janela
        self.mapa = mapa

        self.posX = posM(x)
        self.posY = posM(y)

        self.lista = []

        for a in range(0, 40):
            for b in range(0, 40):
                self.lista.append(Chao(self.janela, self.mapa, (pos(a) + self.posX), (pos(b) + self.posY)))

    def atualizar(self):
        for a in self.lista:
            a.atualizar()

    def salvar(self):
        pass
