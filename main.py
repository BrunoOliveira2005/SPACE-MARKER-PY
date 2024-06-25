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


estrelas = [] #<-- Transformar em dicionario e ajeitar o codigo 


def criarEstrelas():
    posicaoMouse = pygame.mouse.get_pos()
    nomeEstrela = simpledialog.askstring("Space Marker", "Nome da Estrela:", parent=root)
    if not nomeEstrela:
        nomeEstrela = 'Desconhecido'
    estrelas.append((posicaoMouse, nomeEstrela))

def verificaDB():
    try:
        arquivo = open("database.estrelas","r")
        arquivo.close()
        return ""
    except:
        arquivo = open("database.estrelas","w")
        arquivo.close()
        return "Banco de Dados Criado com Sucesso!"
        

def salvarPontos():
    arquivo = open("database.estrelas","a",encoding= "utf-8")
    arquivo.write(estrelas + "\n")
    arquivo.close()
    return "Estrelas salvas com sucesso!"

        

def carregarPontos():
    try:
        arquivo = open("database.estrelas","r",encoding= "utf-8")
        listaEstrelas = arquivo.readlines()
        arquivo.close()
        for posicao, nome in listaEstrelas:
            pygame.draw.circle(tela, branco, posicao, 3, 0)
            idEstrela = fonte.render(nome, True, branco)
            tela.blit(idEstrela, (posicao[0] + 10, posicao[1]))
    except:
        return "Não há estrelas para carregar"


def deletarPontos():
    try:
        arquivo = open("database.estrelas","r",encoding="utf-8")
        listaEstrelas = arquivo.readlines()
        listaEstrelas.pop(all)
        arquivo.close()
    except:
        return "Não há estrelas para deletar"

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

    
    for posicao, nome in estrelas:
        pygame.draw.circle(tela, branco, posicao, 3, 0)
        idEstrela = fonte.render(nome, True, branco)
        tela.blit(idEstrela, (posicao[0] + 10, posicao[1]))





    pygame.display.update()
    clock.tick(60)