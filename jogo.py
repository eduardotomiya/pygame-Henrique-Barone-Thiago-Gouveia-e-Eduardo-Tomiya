import pygame # Importar funções da biblioteca Pygame
import random # Importar funções randomicas
from blocos import Block # Comunicar a pasta responsável por blocos do jogo
from jogador import player # Comunicar a pasta responsável pelo jogador

pygame.init()

largura = 1000 # Dimensão de largura da tela
altura = 1000 # Dimensão de largura da tela

# Configurações do fundo
fundo = pygame.image.load('BH1.tiff') # Foto do fundo atualizando
fundo = pygame.transform.scale(fundo, (largura,altura)) # Ajustar fundo às dimensões da tela
fundo_inicio = pygame.image.load('BH1.tiff') # Foto do fundo da tela inicial
fundo_inicio = pygame.transform.scale(fundo_inicio,(largura,altura))
janela = pygame.display.set_mode((largura,altura)) # Criação da janela utilizada para rodar o jogo
pygame.display.set_caption("Quebra-gelos") # Nome do jogo na Tela Inicial

#Configurações de som
tocabloco = pygame.mixer.Sound('Ice Sound.mp3') # Som de quando bola encosta em blocos
tocatile = pygame.mixer.Sound('TileHit.mp3') # Som de quando bola encosta no bloco do jogador
somfundo = pygame.mixer.Sound('BGMusic.mp3') # Som de fundo do jogo
tocatile.set_volume(.5) # Define som mais baixo para quando bola encosta no bloco do jogador

#Configurações de Tela Inicial
colorwhite = pygame.Color((255,255,255)) # Criação de variável com cor branca
tipoletra = pygame.font.Font('Kaph-Italic.ttf', 60) # Comunicar fonte e tamanho para título
tipoletra2 = pygame.font.Font('Kaph-Italic.ttf', 10) # Comunicar fonte e tamanho para comandos
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



#Definindo as cores

blue = pygame.Color('blue')
pink = pygame.Color('deeppink')
orange = pygame.Color('firebrick1')
yellow = pygame.Color('gold')
green = pygame.Color('green')
white = pygame.Color('white')

colors=[blue,pink,orange,yellow,green,white]
#Cor aleatória para o jogador
cor_jogo=random.choice(colors)
#Cor aleatória bloco
cor_blocos=random.choice(colors)
#A bolinha sempre será azul
cor_bolinha=blue


#Criando instâncias das classes player, bolinha e 
player=player(largura/2 - 50, altura-100,140,20, cor_jogo)
ball = Bolinha(largura/2-10, altura-400,20,20,cor_bolinha)
balls = [Bolinha]


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

# Main Loop Core Jogo
jogo = True
somfundo.stop()
while jogo == False and game == False:
    timer.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False
    if not gameo:
        for bolinha in balls:
            bolinha.move()
        if pygame.mouse.get_pos()[0] - player.c//2 < 0:
            player.a = 0
        elif pygame.mouse.get_pos()[0] + player.c//2 > largura:
            player.a = largura - player.c
        else:
            player.a = pygame.mouse.get_pos()[0] - player.c//2

        for bolinha in balls:
            if (bolinha.a >= player.a and bolinha.a <= player.a + player.c) or (bolinha.a + bolinha.c >= player.a and bolinha.a +ball.c <= player.a + player.c):
                if bolinha.b + bolinha.d >= player.b and bolinha.b + bolinha.d <= player.b + player.d:
                    bolinha.be *= -1
                    bolinha.b = player.b - bolinha.d -1
                    tocatile.play()
            if bolinha.a + bolinha.c >= largura:
                tocatile.play()
                bolinha.ae *= -1
            if bolinha.a < 0:
                tocatile.play()
                bolinha.ae *= -1
            if bolinha.b <= 0:
                tocatile.play()
                bolinha.be *= -1
            if bolinha.b > altura:
               balls.pop(balls.index(bolinha))
        
        for bloco in blocos:
           for bolinha in balls:
               if (bolinha >= bolinha.a and bolinha.a <= bloco.a + bloco.c) or bolinha.a + bolinha.c >= bloco.a and bolinha.a + bolinha.c <= bloco.a + bloco.c:
                   if (bolinha.b >= bloco.b and bolinha.b <= bloco.b + bloco.d) or bolinha.b + bolinha.d >= bloco.b and bolinha.b + bolinha.d <= bloco.b + bloco.d:
                       bloco.visible = False
                       if bloco.pregnant:
                           cor_bola = (0,0,200)
                           balls.append(bolinha(bloco.a, bloco.b, 20, 20, cor_bola))
                       #bricks.pop(bricks.index(brick))
                       bolinha.be *= -1
                       tocabloco.play()
                       break
        
        for bloco in blocos:
           if bloco.visible == False:
               blocos.pop(blocos.index(bloco))


        if len(balls) == 0:
           gameo = True

    chaves = pygame.key.get_pressed()
    if len(blocos) == 0:
       vencer = True
       gameo = True
    if gameo:
       if chaves[pygame.K_SPACE]:
           gameo = False
           vencer = False
           cor_bola = (0,0,200)
           ball = bolinha(largura/2 - 10, altura - 400, 20, 20, cor_bola)
           bolas = [ball]
           if len(bolas) == 0:
               bolas.append(ball)


           blocos.clear()
           for i in range(6):
               for j in range(10):
                   cor_bloco = random.choice(colors)
                   blocos.append(bloco(10 + j * 79, 50 + i * 35, 70, 25, cor_bloco))
    novajanelajogo()
    janela.fill(colorwhite)
    janela.blit(fundo, (0,0))

#Texto final--------------------------------------------------
#Texto caso o player vença
end_txt = tipoletra.render('Bom Jogo!', False, white)
#Texto caso o player perca
end1_txt = tipoletra.render('Volte Novamente!', False, white)
#Texto quando jogador sair do jogo
end2_txt = tipoletra.render('Até mais!', False, white)
#Tela Final----------------------------------
end = True
somfundo.play()
# Loop para rodar a tela final
while end:
# Verifica ocorrência de inputs por jogador
   for evento in pygame.evento.get():
# Verifica se o jogador fechou a tela
       if evento.type == pygame.QUIT:
# Define variável para False e para o loop de tela inicial
           end = False
       if evento.type == pygame.KEYDOWN:
# Verifica se player clicou na key espaço
           if evento.key == pygame.K_SPACE:
# Define variável para False e para o loop de tela inicial
               end = False
# Define fill da janela para cor branca
   janela.fill(white)
   janela.blit(somfundo,(0,0))
   janela.blit(end_txt, (200, 100 ))
   janela.blit(end1_txt, (30, 500))
   janela.blit(end2_txt, (90, 600))
# Aplica novas mudanças à tela inicial
   pygame.display.update()

