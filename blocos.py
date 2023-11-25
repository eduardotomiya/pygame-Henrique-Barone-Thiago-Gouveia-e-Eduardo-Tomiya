import pygame
import random 

class Block(object):
    def inicio(self,a,b,c,d):
#Definição da posição e do tamanho do bloco
        self.a = a
        self.b = b
        self.c= c
        self.d = d
#Cor do bloco(azuk claro)    
        self.color=(173,216,230)
#Valor alfa para transparência(128 para ficar meio transparente)
        self.alpha=128
#Indicação para o bloco ser visível
        self.visible=True
#Cálculo das coordenadas 
        self.aa= self.a +self.c
        self.bb= self.b+self.d
#Geração de um número aleatório 
        self.parte= random.randint(0,10)

        if self.parte<3:
            self.permanente=True
        else:
            self.permanente=False

    def desenho(self, vitoria):
#Criando uma cópia da cor com o valor alpha
        cor_alpha=(*self.color, self.alpha)
#Desenho do bloco
        pygame.desenho.rect(vitoria, cor_alpha,[self.a, self.b, self.c, self.d])
