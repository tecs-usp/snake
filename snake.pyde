from __future__ import division, print_function # Usa partes do Python 3 
# ('/' como divisão real e 'print' como função.)

# 'Hack' para usar atributos nas variáveis.
# Outra possibilidade (mais prolixa) seria usar um dict.
class Segmento: 
    pass

# Formato da cobra (cauda é o elemento zero; cabeça é o último elemento):
#   0  1   2   3   4   5     6
#                           ____
#     _____________________/ O  \___/
# <###___|___|___|___|___|______/   \    
cabeca = Segmento()
cobra = [cabeca]

class Comestiveis:
    pass
comida = Comestiveis() 

# Valores fixos usados por outras partes do jogo.
cinza_cobra = color(200)
verde_cobra = color(103, 175, 43)
vermelho_fim_de_jogo = color(220, 50, 30)
tamanho = 50 # Tamanho dos segmentos e da comida.
npassos = 60 # Distância que cada segmento anda com um passo.
posicao_inicial_x = 420 # Múltiplo de npassos perto do centro. (width/2//npassos*npassos)
posicao_inicial_y = 420
quadros_ate_mover = 6 # Cobra demora para dar cada passo.

def iniciar_cabeca():
    cabeca.x = posicao_inicial_x 
    cabeca.y = posicao_inicial_y
    cabeca.dir = "O"
    cabeca.cor = verde_cobra
              
def desenhar_jogador():
    background(35)
    
    for segm in cobra:
        fill(segm.cor)
        square(segm.x, segm.y, tamanho)

def keyPressed():
    """Função especial que é executada TODA vez que alguma tecla é pressionada. (Mesmo que ela não vá fazer nada!)"""
    global estado
    global pausado ###
    global quadros_ate_mover ###
    
    if key == "q": ### pra ficar mais facil de fechar a janela
        exit()
    if key == "s": ### slow; alterna entre 1x e 0.1x
        quadros_ate_mover = 60/ (1+ 9*(quadrosatemover==60))
    if key == " ": #espaço
        if estado == "inicio" or estado == "fim":
            estado = "jogando"
        elif estado == "jogando": ###
            pausado = not pausado
            debug_info()

    # Dá pra tirar o if key==CODED e deixar tudo junto, mas ainda vai ter que usar o keyCode em vez do key para essas teclas.
    if key == CODED:
        # Verificação de direção da cabeça para evitar que a pessoa perca por andar para trás.
        if keyCode == UP and cabeca.dir != "S":
            cabeca.dir = "N"
        if keyCode == DOWN and cabeca.dir != "N":
            cabeca.dir = "S"
        if keyCode == LEFT and cabeca.dir != "L":
            cabeca.dir = "O"
        if keyCode == RIGHT and cabeca.dir != "O":
            cabeca.dir = "L"
            
def mover_jogador():
    for segm in cobra: #comecamos pela cauda
        
        direcao = segm.dir
        if direcao == "N":
                segm.y -= npassos
        if direcao == "S":
                segm.y += npassos
        if direcao == "L":
                segm.x += npassos
        if direcao == "O":
                segm.x -= npassos
        
        if segm != cabeca:
            numero_segm = cobra.index(segm) # Descobre o número do segmento.
            segm_na_frente = cobra[numero_segm+1] # Pega o próximo segmento.
            
            # Imita o Segmento na frente.
            segm.dir = segm_na_frente.dir
            segm.x = segm_na_frente.x
            segm.y = segm_na_frente.y
            
def nao_deixar_fugir():
    """Mantém a cobra na tela, passando ela para o outro lado se ela fosse sair."""
    if cabeca.x < 0:
        cabeca.x += width
    if cabeca.x > width:
        cabeca.x -= width
    if cabeca.y < 0:
        cabeca.y += height
    if cabeca.y > height:
        cabeca.y -= height
    
def desenhar_comida():
    cor = color(random(256), random(256), random(256))
    fill(cor)
    circle(comida.x, comida.y, tamanho)

def criar_comida():
    """Muda a posição da comida para um valor aleatório."""
    numero_de_setores = width/npassos
    setor_sorteado = int(random(numero_de_setores))
    
    comida.x = npassos*setor_sorteado
    
    numero_de_setores = height/npassos
    setor_sorteado = int(random(numero_de_setores))
    
    comida.y = npassos*setor_sorteado

def tentar_comer():
    """Se a cabeça está na mesma posição que a comida, a cobra cresce em um segmento
    e a próxima comida é posicionada."""
    if cabeca.x == comida.x and cabeca.y == comida.y:
        criar_comida()
        crescer()

def crescer():
    """Insere um segmento na ponta da cauda da cobra."""
    segm = Segmento()
    ponta = cobra[0] # Ponta da cauda, ou seja, o primeiro elemento da cobra.

    segm.x = ponta.x
    segm.y = ponta.y
    segm.dir = ponta.dir
    segm.cor = cinza_cobra
    cobra.insert(0, segm)
        
def no_na_cobra():
    """Se a cabeça da cobra está passando por ela mesma, acaba o jogo."""
    
    global estado
    
    for segm in cobra:
        if segm != cabeca:
            if cabeca.x == segm.x and cabeca.y == segm.y:
                estado = "fim"
    
def tela_de_inicio():
    """Mostra a tela de início."""
    background(35)
    textAlign(CENTER, CENTER)
    textSize(210)
    fill(verde_cobra)
    text("Snake", width/2, height/2)
    fill(color(255))
    textSize(40)
    text("(Aperte espaco para iniciar!)", width/2, height/2+200) # Nota: sem unicode.
    
def fim_de_jogo():
    """Mostra a tela de fim de jogo."""
    
    global cobra
    
    # Preparamos para reiniciar o jogo.
    iniciar_cabeca()
    cobra = [cabeca] # Tira todos os segmentos e deixa só a cabeça.
    criar_comida()
    
    # Só começamos a desenhar na tela aqui.
    background(35) # cinza
    textAlign(CENTER, CENTER)
    textSize(68)
    fill(vermelho_fim_de_jogo)
    text("Fim de jogo :(", width/2, height/2)
    fill(color(255)) # branco
    textSize(25)
    text("(Aperte espaco para reiniciar!)", width/2, height/2+150)
    
def setup():
    """Função especial para preparar o início do jogo. 
    Ela é executada assim que iniciamos o programa."""
    
    global estado, pausado
    
    size(900, 900)
    noCursor()
    rectMode(CENTER)
    background(35)
    
    iniciar_cabeca()
    criar_comida()
    estado = "inicio"
    pausado = False

def draw():
    """Função especial que é a função central do programa. 
    É ela que vai executar outras funções e controlar o nosso jogo.
    IMPORTANTE: no Processing, esta função é executada automaticamente para todo o sempre! 
    setup() só é executada uma vez, mas draw() é executada até o programa ser fechado."""
    
    if estado == "inicio":
        tela_de_inicio()
    if estado == "jogando" and pausado == False: ###
        principal()
    if estado == "fim":
        fim_de_jogo()
        
def pode_mover():
    """Diz se já é hora da cobra se mover. Se ela sempre pudesse se mover, ela seria rápida demais!"""
    quadroatual = frameCount
    resposta = (quadroatual % quadros_ate_mover == 0)
    return resposta

def coords(): ###
    fill(color(255))
    textSize(20)
    text("comida: ({0:^3}, {1:^3})".format(comida.x,comida.y), 100, 15)
    text("jogador: ({0:^3}, {1:^3})".format(cabeca.x,cabeca.y), 350, 15)

def debug_info():
    ### Acho que está tudo ok?
    print("frame:",frameCount)
    print("comida:", "({0:^5},{1:^5})".format(comida.x, comida.y))
    print("cobra:")
    for i in range(len(cobra)):
        print("\t", i, ":", "({0:^5},{1:^5},{2:^3})".format(cobra[i].x, cobra[i].y, cobra[i].dir), sep="", end="")
        flechatalvez = (i==0)*" <---------- ponta da cauda" + (i==len(cobra)-1)*" <---------- cabeca"
        print(flechatalvez)
    print("ultimo segmento eh a cabeca?", "NAAAAO "*(cabeca!=cobra[-1]) +"eh!")
    print(id(cabeca),id(cobra[-1]))
    
def principal():
    """Instruções principais do jogo que são re-executadas continuamente."""
    desenhar_jogador()
    desenhar_comida()
    coords()
    
    if pode_mover():
        mover_jogador()
        nao_deixar_fugir()
        no_na_cobra() # no_na_cobra() sempre antes do tentar_comer()
        tentar_comer()
    
