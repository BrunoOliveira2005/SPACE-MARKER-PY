import pygame
import os 
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




branco  = (255,255,255)
preto = (0,0,0)


estrelas = []


def criarEstrelas(): # o nome das estrela n ta alinhado no ponto da estrela 
    posicaoMouse = pygame.mouse.get_pos()
    estrelas.append(posicaoMouse)
    nomeEstrela = simpledialog.askstring("Space Marker","Nome da Estrela:")
    idEstrela = fonte.render(nomeEstrela,True,branco)
    tela.blit(idEstrela,(posicaoMouse))
    for posicao in estrelas:                                    
            pygame.draw.circle(tela,branco,posicao,3,0)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            criarEstrelas()



    #tela.blit(fundo,(0,0)) 





    pygame.display.update()
    clock.tick(60)