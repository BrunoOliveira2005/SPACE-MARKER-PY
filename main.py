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


branco = (255, 255, 255)
preto = (0, 0, 0)
estrelas = {} 


def criarEstrelas():
    posicaoMouse = pygame.mouse.get_pos()
    nomeEstrela = simpledialog.askstring("Space Marker", "Nome da Estrela:", parent=root)
    if not nomeEstrela:
        nomeEstrela = 'Desconhecido'
    estrelas[posicaoMouse]= nomeEstrela

def verificaDB():
    if os.path.exists("database.estrelas"):
        return ""
    else:
        with open("database.estrelas", "w") as arquivo:
            arquivo.close()
        return "Banco de Dados Criado com Sucesso!"
        

def salvarPontos():
    with open("database.estrelas", "w", encoding="utf-8") as arquivo:
        for posicao, nome in estrelas.items():
            arquivo.write(f"{posicao[0]},{posicao[1]},{nome}\n")
    return "Estrelas salvas com sucesso!"

        

def carregarPontos():
    try:
        with open("database.estrelas", "r", encoding="utf-8") as arquivo:
            listaEstrelas = arquivo.readlines()
        for linha in listaEstrelas:
            x, y, nome = linha.strip().split(",")
            estrelas[(int(x), int(y))] = nome
    except:
        return "Não há estrelas para carregar"

def deletarPontos():
    if os.path.exists("database.estrelas"):
        os.remove("database.estrelas")
    estrelas.clear()
    return "Estrelas deletadas com sucesso!"

verificaDB()
carregarPontos()

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            criarEstrelas()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F10:
            salvarPontos()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F11:
            carregarPontos()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F12:
            deletarPontos()

    tela.blit(fundo,(0,0)) 
    textoComandos = fonte.render("F10 -> Salvar Estrelas "+"F11 -> Carregar Estrelas "+"F12 -> Deletar Estrelas",True,branco)
    tela.blit(textoComandos,(10,10))

    
    for posicao, nome in estrelas.items():
        pygame.draw.circle(tela, branco, posicao, 3, 0)
        textoEstrela = f"{nome} ({posicao[0]}, {posicao[1]})"
        idEstrela = fonte.render(textoEstrela, True, branco)
        tela.blit(idEstrela, (posicao[0] + 10, posicao[1]))

    if len(estrelas) > 1:
        pontos = list(estrelas.keys())
        pygame.draw.lines(tela, branco, False, pontos, 1)


    pygame.display.update()
    clock.tick(60)

    