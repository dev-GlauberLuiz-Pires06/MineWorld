import pygame
from pygame.draw import *
from auxilio import *

class Persona:
    def __init__(self, janela, mapa, x, y):
        self.janela = janela
        self.mapa = mapa

        self.posX = x
        self.posY = y
        self.tamX = 26
        self.tamY = 26

        self.vel = 9
        self.veld = 6

    def atualizar(self, keys):

        numt = False
        numero = 0

        if keys[0] == True:
            numero = numero + 1
        if keys[1] == True:
            numero = numero + 1
        if keys[2] == True:
            numero = numero + 1
        if keys[3] == True:
            numero = numero + 1

        if numero >= 2:
            numt = True

        if numt == True:
            if keys[0] == True and keys[1]:
                self.posX = self.posX - self.veld
                self.posY = self.posY - self.veld
            if keys[1] == True and keys[3]:
                self.posX = self.posX + self.veld
                self.posY = self.posY - self.veld
            if keys[2] == True and keys[3]:
                self.posX = self.posX + self.veld
                self.posY = self.posY + self.veld
            if keys[0] == True and keys[2]:
                self.posX = self.posX - self.veld
                self.posY = self.posY + self.veld

        if numt == False:
            if keys[0] == True:
                self.posX = self.posX - self.vel
            if keys[1] == True:
                self.posY = self.posY - self.vel
            if keys[2] == True:
                self.posY = self.posY + self.vel
            if keys[3] == True:
                self.posX = self.posX + self.vel

        self.mapa.posX = - self.posX + 670
        self.mapa.posY = - self.posY + 330

        rect(self.janela, BLUE, ((self.posX + self.mapa.posX), (self.posY + self.mapa.posY), self.tamX, self.tamY))
