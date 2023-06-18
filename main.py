import pygame
#Aqui vou usar uma biblioteca chamada tkinter.
from tkinter import simpledialog
pygame.init()
#Aqui temos o tamanho do nosso Space Marker.
tamanho = (800,600)
#Aqui temos a trilha sonora.
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
#Aqui temos o Nome do programa quando é aberto.
pygame.display.set_caption("Space Maker")
#Aqui temos a imagem de fundo.
fundo = pygame.image.load("bg.jpg")
tela = pygame.display.set_mode( tamanho )
#Aqui temos a imagem utilizada como icone do programa.
pygame.display.set_icon(pygame.image.load("space.png"))
running = True 
#Cor branca.
branco = (255,255,255)
itens = []

#Isso é o raio do circulo criado quando adicioando uma estrela.
raio = 3
circulos = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space" , "Nome da Estrela:")
            print(item)
            if item == "":
                item = "desconhecido"+str(pos)
            else:
                item = item + str(pos)
            itens.append((item, pos))
            
            


    tela.blit(fundo,(0,0))
    for item , pos in itens:
        mensagemDisplay = pygame.font.SysFont(None, 24).render (item , True , branco)
        tela.blit(mensagemDisplay, pos)
        pygame.draw.circle(tela , branco , pos , raio)


    pygame.display.update()

pygame.quit()