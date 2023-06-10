import pygame
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tela.blit(fundo,(0,0))

    pygame.display.update()

pygame.quit()