#Inicio do Programa
import pygame
import random

pygame.init() #iniciando o pygame
pygame.display.set_caption("Snake Game em Python") #Título da janela
largura, altura = 1200, 800 #Tamanho da janela
tela = pygame.display.set_mode((largura, altura)) #importacao do tamanho para o pygame
relogio = pygame.time.Clock() #variavel para tempo

#Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

#Dimensoes Gerais
tamanho_quadrado = 20
velocidade = 15

def desenhar_titulo():
    fonte = pygame.font.SysFont("Helvetica", 25)
    texto = fonte.render("Snake Game em Python", True, branco)
    tela.blit(texto, [1, 1])

def gerar_comida():
   comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
   comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
   return comida_x, comida_y

def gerar_bomba():
   bomba_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
   bomba_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
   return bomba_x,bomba_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_bomba(tamanho, bomba_x, bomba_y):
    pygame.draw.rect(tela, vermelho, [bomba_y, bomba_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0],pixel [1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 25)
    texto = fonte.render(f"Pontos: {pontuacao}", True, branco)
    tela.blit(texto, [1, 30])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def  rodar_jogo():
    fim_jogo = False

    x = largura/2
    y = altura/2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    #Gerando a primeira comida
    comida_x, comida_y = gerar_comida()

    #Gerando a primeira bomba
    bomba_x, bomba_y = gerar_bomba()

    while not fim_jogo:
        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        #Gerando Bomba
        desenhar_bomba(tamanho_quadrado, bomba_x, bomba_y)
        #Gerando comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        #Atualizando a posição da cobra
        if x < 0 or x >= largura or y < 0 or y>= altura:
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y

        #gerando Cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # Validando se a cobra bateu no seu corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        #Gerando titulo
        desenhar_titulo()

        #Gerando cobra
        desenhar_cobra(tamanho_quadrado, pixels)

        #gerando pontos
        desenhar_pontuacao(tamanho_cobra -1)

        #Atualização tela
        pygame.display.update()

        #Gerar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = (gerar_comida())
        elif x == bomba_x and y == bomba_y:
            fim_jogo = True
        else:
            bomba_x, bomba_y = (gerar_bomba())
        relogio.tick(velocidade)
rodar_jogo()


