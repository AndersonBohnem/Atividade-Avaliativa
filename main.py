import pygame
import ast
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
#Essa é a fonte dos comandos.(F10,F11,F12)
fonte = pygame.font.Font(None, 24)

def Salvar():
    try:
        arquivo = open("SalvarPontos.txt","w")
        for item in itens:
            arquivo.write("{0}\n".format(item))
        arquivo.close()
    except:
        print("Erro ao salvar")

#Isso é o raio do circulo criado quando adicioando uma estrela.
raio = 3


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Salvar()
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
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            Salvar()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Salvar()
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            try:
                arquivo = open("SalvarPontos.txt","r")
                linhas = arquivo.readlines()
                for item in linhas:
                    tupla = ast.literal_eval(item)
                    itens.append(tupla)



            except:
                print("Erro ao carregar os arquivos")



        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            arquivo = open("SalvarPontos.txt","w")
            itens=[]
            arquivo.close()            
                    



    f10 = fonte.render("Pressione F10 para salvar os Pontos", True , branco)
    f11 = fonte.render("Pressione F11 para carregar as marcações salvas", True, branco)
    f12 = fonte.render("Pressione F12 para excluir todas as marcações", True, branco)


    #Essa linha é para o fundo.
    tela.blit(fundo,(0,0))
    #Essas linhas é para exibir os comandos (F10,F11,F12)
    tela.blit(f10, (10,10))
    tela.blit(f11, (10,30))
    tela.blit(f12, (10,50))
    #Esse for é resonsavel por adicionar a escrita depois da caixa de pergunta.
    primeiro = True
    coord1 = ()
    coord2 = ()
    for item, pos in itens:
        mensagemDisplay = pygame.font.SysFont(None, 24).render (item , True , branco)
        tela.blit(mensagemDisplay, pos)
        pygame.draw.circle(tela , branco , pos , raio)
        if primeiro == True:
            coord1 = pos
            primeiro = False
        else:
            coord2 = pos
            pygame.draw.line(tela, branco, coord1, coord2, 1)
            coord1= pos




    pygame.display.update()

pygame.quit()