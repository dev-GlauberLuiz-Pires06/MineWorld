from pygame.draw import *
from auxilio import *

class Main_C:
    def __init__(self, janela, x, y):
        self.janela = janela
        # self.mundo = mundo

        # =========================
        # -- qualidades --

        # basicas
        self.posX = x
        self.posY = y
        self.tamX = 32
        self.tamY = 32
        self.cor = GREEN1
        # =========================

    def atualizar(self):
        rect(self.janela, self.cor, ((self.posX), (self.posY), self.tamX, self.tamY))
        rect(self.janela, BLACK, ((self.posX), (self.posY), self.tamX, self.tamY), 1)
