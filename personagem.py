import pygame
from auxilio import *

class Personagem:
    def __init__(self, janela, ponto_de_referencia, x, y):
        self.janela = janela
        self.PDR = ponto_de_referencia

        self.posX = x
        self.posY = y
        self.tamX = 26
        self.tamY = 26

        self.veloc = 12
        self.velocD = 8

    def atualizar(self, teclas):

        # movimentação
        velocX = 0
        velocY = 0
        duas_num = 0
        duas = False
        for a in range(0, 4):
            if teclas[a] == True:
                duas_num = duas_num + 1

        if duas_num >= 2:
            duas = True

        if duas == False:
            if teclas[T_A]:
                velocX = velocX - self.veloc
            if teclas[T_W]:
                velocY = velocY - self.veloc
            if teclas[T_S]:
                velocY = velocY + self.veloc
            if teclas[T_D]:
                velocX = velocX + self.veloc

        if duas >= True:
            if teclas[T_A] == True and teclas[T_W]:
                velocX = velocX - self.velocD
                velocY = velocY - self.velocD
            if teclas[T_W] == True and teclas[T_D]:
                velocX = velocX + self.velocD
                velocY = velocY - self.velocD
            if teclas[T_D] == True and teclas[T_S]:
                velocX = velocX + self.velocD
                velocY = velocY + self.velocD
            if teclas[T_S] == True and teclas[T_A]:
                velocX = velocX - self.velocD
                velocY = velocY + self.velocD

        self.posX = self.posX + velocX
        self.posY = self.posY + velocY

        pygame.draw.rect(self.janela, BLUE, (self.posX, self.posY, self.tamX, self.tamY))
