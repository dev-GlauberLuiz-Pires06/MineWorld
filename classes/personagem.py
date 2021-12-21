from pygame.draw import *
from auxilio import *

class Main_PS:
    def __init__(self, janela, mundo, x, y):
        self.janela = janela
        self.mundo = mundo

        # =========================
        # -- qualidades --

        # basicas
        self.posX = x
        self.posY = y
        self.tamX = 32
        self.tamY = 32
        # =========================

    def atualizar(self):
        pass
