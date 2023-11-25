import pygame # Importar funções da biblioteca Pygame
import random # Importar funções randomicas
from blocos import Bloco # Comunicar a pasta responsável por blocos do jogo
from jogador import jogador # Comunicar a pasta responsável pelo jogador

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
