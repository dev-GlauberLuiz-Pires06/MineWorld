from pygame.draw import *
from auxilio import *
from classes import chao

class Main_Slot:
    def __init__(self, janela, x, y):
        self.janela = janela

        self.posX = x
        self.posY = y

        self.lista = []

        for a in range(0, 8):
            for b in range(0, 8):
                self.lista.append(chao.Main_C(self.janela, (a * 32), (b * 32)))

    def atualizar(self):
        for obj in self.lista:
            obj.atualizar()
