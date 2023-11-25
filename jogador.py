import pygame

#definição da classe do jogador

class player(object):
#Início da definição da classe com parâmetros de posição, largura, altura e cor
    def inicio(self, a, b, c, d, color):
       self.a =a

       self.b =b

       self.c =c

       self.d =d

       self.color = color
#cálculo das coordenadas do canto inferior direito do retângulo
       self.aa = self.a + self.c
       self.bb = self.b + self.d
#Desenho do jogador
    def desenho(self, vitoria):
#Desenho do retângulo
        pygame.desenho.rect(vitoria, self.color, [self.a, self.b, self.c, self.d])