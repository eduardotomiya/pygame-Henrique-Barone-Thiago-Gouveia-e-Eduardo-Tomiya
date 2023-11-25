import pygame # Importar funções da biblioteca Pygame
import random # Importar funções randomicas
from blocos import Bloco # Comunicar a pasta responsável por blocos do jogo
from jogador import jogador # Comunicar a pasta responsável pelo jogador

pygame.init()

width = 1000 # Dimensão de largura da tela
height = 1000 # Dimensão de largura da tela

# Configurações do fundo
Fundo = pygame.image.load

