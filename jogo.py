import pygame # Importar funções da biblioteca Pygame
from blocos import Bloco # Comunicar a pasta responsável por blocos do jogo
from jogador import jogador # Comunicar a pasta responsável pelo jogador
from bolas import circle

pygame.init()

largura = 905 # Dimensão de largura da tela
altura = 800 # Dimensão de largura da tela

# Configurações do fundo
fundo = pygame.image.load('BH1.tiff') # Foto de fundo
fundo = pygame.transform.scale(fundo, (largura,altura)) # Ajustar fundo às dimensões da tela
fundo_inicio = pygame.image.load('SpaceInit.png') # Foto do fundo da tela inicial
fundo_inicio = pygame.transform.scale(fundo_inicio,(largura,altura))
janela = pygame.display.set_mode((largura, altura)) # Criação da janela utilizada para rodar o jogo
pygame.display.set_caption('Space Cruiser') # Nome do jogo na Tela Inicial

#Configurações de som
tocabloco = pygame.mixer.Sound('Ice Sound.mp3') # Som de quando bola encosta em blocos
tocatile = pygame.mixer.Sound('TileHit.mp3') # Som de quando bola encosta no bloco do jogador
somfundo = pygame.mixer.Sound('BGMusic.mp3') # Som de fundo do jogo
tocatile.set_volume(.2) # Define som mais baixo para quando bola encosta no bloco do jogador

#Configurações de Tela Inicial
colorwhite = pygame.Color('grey100') # Criação de variável com cor branca
tipoletra = pygame.font.Font('Kaph-Italic.ttf', 60) # Comunicar fonte e tamanho para título
textoinicial = tipoletra.render('Space Cruiser', False, colorwhite) # Aparecer nome do Jogo
texto1 = tipoletra.render('Pressione Espaço', False, colorwhite) # Aparecer comando para iniciar o jogo
texto2 = tipoletra.render('para começar', False, colorwhite) # Continuar comando para iniciar o jogo

# Funcionamento Tela Inicial
work = True # Define variável que para o jogo quando definida para False
while work: # Loop para rodar a tela inicial
    for evento in pygame.event.get(): # Verifica ocorrência de inputs por jogador
        if evento.type == pygame.QUIT: # Verifica se o jogador fechou a tela
            work = False # Define variável para False e para o loop de tela inicial
        if evento.type == pygame.KEYDOWN: # Verifica inputs de teclas por jogador
            if evento.key == pygame.K_SPACE: # Verifica se tecla é espaço
                work = False # Define variável para False e para o loop de tela inicial
    janela.fill(colorwhite) # Define fill da janela para cor branca
    janela.blit(fundo_inicio,(0,0))
    janela.blit(textoinicial, (140, 100))
    janela.blit(texto1, (80, 500))
    janela.blit(texto2, (150, 600))
    somfundo.play() # Da play no som de fundo
    pygame.display.update() # Atualiza novas condições de jogo

timer = pygame.time.Clock() # Define tempo do jogo
FPS = 200 # Definição do jogo em Frames Por Segundo

# Funções Main do Jogo
blocos = [] 
def init():
    global blocos # Define uma variável global para os blocos
    blocos = [] # Lista para armanzenar comandos da classe blocos
    for i in range(5): # Define tamanho da coluna de blocos
        for j in range(20): # Define tamanho da fileira de blocos
            cor_bloco = (173,216,230) # Define cor dos blocos para azul claro
            blocos.append(Bloco(5 + j * 45, 50 + i * 35, 40, 25, cor_bloco)) # Define parâmetros (x, y, largura, altura e cor) para os blocos
finale = False # Define variável de gameover para uso em if de fim de jogo
def redrawGameWindow(): # Janela principal do jogo
    janela.blit(fundo, (0,0)) # Inicia o fundo da tela de jogo
    Jogador.draw(janela)
    for bolinha in balls: # Loop para bolas na tela
        bolinha.draw(janela) # Desenha bola na tela
    for b in blocos: # Loop para blocos na tela
        b.draw(janela) # Desenha bloco na tela

    endfont = pygame.font.Font('Kaph-Italic.ttf', 25) # Define fonte para escritas futuras

    if finale: # Vericia se gameover é True ou False
        if len(blocos) == 0: # Verifica quantidade blocos
            resText = endfont.render("Bom jogo!", 1, (255, 255, 255)) # Texto de fim de jogo em WIN
        else:
            resText = endfont.render("Que Pena!", 1, (255, 255, 255)) # Texto de fim de jogo em LOSE
        janela.blit(resText, ((largura//2 - resText.get_width()//2), altura//2 - resText.get_height()//2)) # Posição do texto de final
        playAgainText = endfont.render("Pressione Espaço para jogar novamente", 1, (255, 255, 255)) # Texto de reiniciar
        janela.blit(playAgainText, ((largura//2 - playAgainText.get_width()//2), altura//2 + 30 )) # Posição do texto de reinciar

    pygame.display.update() # Atualiza novas condições do jogo

#Definindo as cores e dimensões
playercol = (173,216,230) # Define as cores do bloco do jogador
ballcol = (255,119,0) # Define as cores das bolas
Jogador = jogador(largura/2 - 50,altura-100,140,20,playercol) # Define as dimensões do bloco do jogador
bola = circle(largura/2 - 10, altura - 400, 20, 20, ballcol) # Define as dimensões das bolas
balls = [bola]
init()

# Main Loop Core Jogo
game = True
while game and work == False:
    timer.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game = False
    if not finale:
        for bolinha in balls:
            bolinha.move()
        if pygame.mouse.get_pos()[0] - Jogador.w//2 < 0:
            Jogador.x = 0
        elif pygame.mouse.get_pos()[0] + Jogador.w//2 > largura:
            Jogador.x = largura - Jogador.w
        else:
            Jogador.x = pygame.mouse.get_pos()[0] - Jogador.w //2 # Define posição do bloco do jogador de acordo com posição do mouse

        for bolinha in balls:
            if (bolinha.x >= Jogador.x and bolinha.x <= Jogador.x + Jogador.w) or (bolinha.x + bolinha.w >= Jogador.x and bolinha.x + bolinha.w <= Jogador.x + Jogador.w):
                if bolinha.y + bolinha.h >= Jogador.y and bolinha.y + bolinha.h <= Jogador.y + Jogador.h:
                    bolinha.yv *= -1
                    bolinha.y = Jogador.y -bolinha.h -1
                    tocatile.play()

            if bolinha.x + bolinha.w >= largura:
                tocatile.play()
                bolinha.xv *= -1
            if bolinha.x < 0:
                tocatile.play()
                bolinha.xv *= -1
            if bolinha.y <= 0:
                tocatile.play()
                bolinha.yv *= -1

            if bolinha.y > altura:
                balls.pop(balls.index(bolinha))

        for bloco in blocos:
            for bolinha in balls:
                if (bolinha.x >= bloco.x and bolinha.x <= bloco.x + bloco.w) or bolinha.x + bolinha.w >= bloco.x and bolinha.x + bolinha.w <= bloco.x + bloco.w:
                    if (bolinha.y >= bloco.y and bolinha.y <= bloco.y + bloco.h) or bolinha.y + bolinha.h >= bloco.y and bolinha.y + bolinha.h <= bloco.y + bloco.h:
                        bloco.visible = False
                        if bloco.pregnant:
                            ballcol = (255,119,0)
                            balls.append(circle(bloco.x, bloco.y, 20, 20, ballcol))
                        #bricks.pop(bricks.index(brick))
                        bolinha.yv *= -1
                        tocabloco.play()
                        break

        for bloco in blocos:
            if bloco.visible == False:
                blocos.pop(blocos.index(bloco))

        if len(balls) == 0:
            finale = True

    teclas = pygame.key.get_pressed()
    if len(blocos) == 0:
        venceu = True
        finale = True
    if finale:
        if teclas[pygame.K_SPACE]:
            finale = False
            venceu = False
            ballcol = (255,119,0)
            bola = circle(largura/2 - 10, altura - 400, 20, 20, ballcol)
            balls = [bola]
            if len(balls) == 0:
                balls.append(bola)

            blocos.clear()
            for i in range(5): # Define tamanho da coluna de blocos
                for j in range(20): # Define tamanho da fileira de blocos
                    cor_bloco = (173,216,230) # Define cor dos blocos para azul claro
                    blocos.append(Bloco(5 + j * 45, 50 + i * 35, 40, 25, cor_bloco)) # Define parâmetros (x, y, largura, altura e cor) para os blocos
    redrawGameWindow()
    janela.fill(colorwhite)
    janela.blit(fundo, (0,0))

#Texto final
textoend = tipoletra.render('Bem Jogado!', False, colorwhite) # Texto caso o player vença
texto1end = tipoletra.render('Volte novamente!', False, colorwhite) # Texto para quando jogador sai do jogo
texto2end = tipoletra.render('Até mais!', False, colorwhite) # Texto para quando jogador sai do jogo

#Tela Final
tchau = True # Variavel para rodar loop final
somfundo.play() # Play no som de final
while tchau: # Loop para rodar a tela final
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            tchau = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                tchau = False
    janela.fill(colorwhite)
    janela.blit(fundo_inicio,(0,0))
    janela.blit(textoend, (200, 100 ))
    janela.blit(texto1end, (60, 500))
    janela.blit(texto2end, (250, 600))
    pygame.display.update() # Atualiza novas condições do jogo