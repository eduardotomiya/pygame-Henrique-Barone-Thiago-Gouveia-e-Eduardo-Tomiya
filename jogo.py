import pygame # Importar funções da biblioteca Pygame
import random # Importar funções randomicas
from blocos import Bloco # Comunicar a pasta responsável por blocos do jogo
from jogador import player # Comunicar a pasta responsável pelo jogador

pygame.init()

largura = 1000 # Dimensão de largura da tela
altura = 1000 # Dimensão de largura da tela

# Configurações do fundo
fundo = pygame.image.load() # Foto do fundo atualizando
fundo = pygame.transform.scale(fundo, (largura,altura)) # Ajustar fundo às dimensões da tela
fundo_inicio = pygame.image.load() # Foto do fundo da tela inicial
fundo_inicio = pygame.transform.scale(fundo_inicio,(largura,altura))
janela = pygame.display.set_mode((largura,altura)) # Criação da janela utilizada para rodar o jogo
pygame.display.set_caption("Quebra-gelos") # Nome do jogo na Tela Inicial

#Configurações de som
tocabloco = pygame.mixer.Sound() # Som de quando bola encosta em blocos
tocatile = pygame.mixer.Sound() # Som de quando bola encosta no bloco do jogador
somfundo = pygame.mixer.Sound() # Som de fundo do jogo
tocatile.set_volume(.5) # Define som mais baixo para quando bola encosta no bloco do jogador

#Configurações de Tela Inicial
colorwhite = pygame.Color((255,255,255)) # Criação de variável com cor branca
tipoletra = pygame.font.Font() # Comunicar fonte e tamanho para título
tipoletra2 = pygame.font.Font() # Comunicar fonte e tamanho para comandos
textoinicial = tipoletra.render('Ice Wrecker', False, colorwhite) # Aparecer nome do Jogo
texto1 = tipoletra2.render('Pressione Espaço para Iniciar', False, colorwhite) # Aparecer comando para iniciar o jogo

# Funcionamento Tela Inicial
game = True # Define variável que para o jogo
while game: # Loop para rodar a tela inicial
    for evento in pygame.event.get(): # Verifica ocorrência de inputs por jogador
       if evento.type == pygame.QUIT: # Verifica se o jogador fechou a tela
           game = False # Define variável para False e para o loop de tela inicial
       if evento.type == pygame.K_SPACE: # Verifica se player clicou na key espaço
           game = False # Define variável para False e para o loop de tela inicial
    janela.fill(colorwhite) # Define fill da janela para cor branca
    janela.blit (fundo_inicio, (0,0))
    janela.blit (textoinicial, (200,100))
    janela.blit (texto1, (30,500))
    somfundo.play() # Toca o som de fundo da tela inicial
    pygame.display.update() # Aplica novas mudanças à tela inicial

timer = pygame.time.Clock() # Define tempo
FPS = 40 # Definição do jogo em Frames Por Segundo

#classe bolinha

class Bolinha(object):
    def inicio(self,a,b,c,d,color):
#Posição e tamanho da bola 
        self.a=a
        self.b=b
        self.c=c
        self.d=d
#Cor da bola(azul)
        self.color=(0,0,255)
#Velocidades iniciais em cada eixo
        self.ae=random.randint(-6,6)
        self.be=6
#Cálculo das coordenadas do canto inferior direito
        self.aa= self.a + self.c
        self.bb= self.b + self.d

    def desenho(self,vitoria):
#Desenho do formato da bola
        pygame.desenho.circle(vitoria,self.color, (self.a, self.b),12,6)
    def move(self):
#Movendo a bola ao longo do eixo x e y
        self.a += self.ae
        self.b += self.be

# Funcionamento Main do Jogo
blocos = []
def inicial():
    global blocos # Define uma variável global para os blocos
    blocos = [] # Lista para armanzenar comandos da classe blocos
    for a in range(5): # Define tamanho da coluna de blocos
        for b in range(15): # Define tamanho da fileira de blocos
            blockcolor = (0,0,100) # Define cor dos blocos para azul claro
            blocos.append() # Define paraâmetros (x, y, largura, altura e cor) para os blocos
gameo = False # Define variável de gameover para uso em if de fim de jogo

def novajanelajogo(): # Janela principal do jogo
    janela.blit(fundo, (0,0)) # Inicia o fundo da tela de jogo
    player.draw(janela)
    for ball in balls: # Loop para bola na tela
        ball.draw(janela) # Desenha bola na tela
    for brick in blocos: # Loop para bloco na tela
        brick.draw(janela) # Desenha bloco na tela
    
    winfont = pygame.font.Font() # Define fonte para endgame

    if gameo: # Vericia se gameover é True ou False
        if len(blocos) == 0: # Verifica quantidade blocos
            textofim = winfont.render('Bem Jogado, Você Venceu!', 1, colorwhite) # Texto de fim de jogo em WIN
        else:
            textofim = winfont.render('Que Pena, Você Perdeu!', 1, colorwhite) # Texto de fim de jogo em LOSE
        janela.blit(textofim, ((largura//2 - textofim.get_width()//2), altura//2 - textofim.get_height()//2)) # Posição do texto de final
        jogonovo = winfont.render('Pressione Espaço para uma Nova Tentativa', 1, colorwhite) # Texto de reiniciar
        janela.blit(jogonovo, (largura//2 - jogonovo.get_width()//2, altura//2 + 35)) # Posição do texto de reinciar

        pygame.display.update() # Atualiza novas condições do jogo