import time
import pygame

# Definindo as dimensões da tela
largura, altura = 1000, 1000

# Criando a janela
janela = pygame.display.set_mode((largura, altura))

# Lista de caminhos para as suas imagens
imagens = ['BH1','BH2','BH3','BH4','BH5','BH6','BH7','BH8','BH9','BH10','BH11','BH12','BH13','BH14','BH15','BH16','BH17','BH18','BH19','BH20','BH21','BH22','BH23','BH24','BH25','BH26','BH27','BH28','BH29','BH30']

# Inicializando variáveis
atual_imagem = 0
# Altere para o intervalo desejado em segundos
tempo = 0.1
tempo_anterior = time.time()


# Loop principal
run = True
while run:
   for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
           run = False


# Verificando se é hora de mudar a imagem
   momento = time.time()
   if momento - tempo_anterior > tempo:
       tempo_anterior = momento


# Carregando a próxima imagem
       imagem_path = imagens[atual_imagem]
       imagem_atual = pygame.image.load(imagem_path)
       imagem_atual = pygame.transform.scale(imagem_atual, (largura, altura))


# Exibindo a imagem na janela
       janela.blit(imagem_atual, (0, 0))


# Atualizando a exibição
       pygame.display.update()


# Avançando para a próxima imagem na lista
       atual_imagem = (atual_imagem + 1) % len(imagens)