import pygame
import os 
import tkinter as tk
from tkinter import simpledialog

pygame.init()


clock = pygame.time.Clock()
tamanho  = (1280,750)
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("assets/icone.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Space Marker")
fundo = pygame.image.load("assets/fundo.jpg")
fonte = pygame.font.SysFont("comicsans",14)

root = tk.Tk()
root.withdraw()


branco  = (255,255,255)
preto = (0,0,0)


estrelas = []


def criarEstrelas(): # o nome das estrela n ta alinhado no ponto da estrela 
    posicaoMouse = pygame.mouse.get_pos()
    nomeEstrela = simpledialog.askstring("Space Marker", "Nome da Estrela:", parent=root)
    if not nomeEstrela:
        nomeEstrela = 'Desconhecido'
    estrelas.append((posicaoMouse, nomeEstrela))

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            criarEstrelas()



    tela.blit(fundo,(0,0)) 

    # Desenhar as estrelas e os nomes
    for posicao, nome in estrelas:
        pygame.draw.circle(tela, branco, posicao, 3, 0)
        idEstrela = fonte.render(nome, True, branco)
        tela.blit(idEstrela, (posicao[0] + 10, posicao[1]))





    pygame.display.update()
    clock.tick(60)