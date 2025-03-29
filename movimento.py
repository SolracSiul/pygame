import pygame

pygame.init()

tamanho_tela = (800,800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Quebra blocos")
#criar bola, ator e bloco
tamanho_bola = 15
bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola)
tamanho_jogador = 100
#recebe, x,y, tamanho e altura
jogador = pygame.Rect(50, 600, tamanho_jogador, 15)


qtd_linhas = 8
qtd_colunas = 5
qtd_total = qtd_linhas * qtd_colunas

def criar_blocos(qtd_linhas, qtd_colunas):
    #pegar altura e largura da tela e reduzir tamanho:
    altura_tela = tamanho_tela[1]
    largura_tela = tamanho_tela[0]
    largura_bloco = largura_tela / 8 - 5 
    altura_bloco =15
    espaco_entre_linhas = altura_bloco + 10
    blocos = []
    for j in range(qtd_colunas):
        for i in range(qtd_linhas):
            bloco = pygame.Rect(i * (largura_bloco + 5) , j * espaco_entre_linhas, largura_bloco, altura_bloco)
            blocos.append(bloco)
    return blocos
#como criar esses blocos
#cores:
cores = {
    "branco": (255,255,255),
    "preto": (0,0,0),
    "amarelo": (255,255,0),
    "azul": (0,0,255),
    "verde": (0,255,0)
}

fim_jogo = False
pontuacao = 0
movimento_bola = [1,1]

# criar as funções do jogo:
def desenhar_inicio_jogo():
    tela.fill(cores["preto"])   
    pygame.draw.rect(tela,cores["azul"], jogador)
    pygame.draw.rect(tela, cores["branco"], bola)
#criar um loop infinito se não ele só abre e fecha
def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["verde"], bloco)

def movimentar_jogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            jogador.x = jogador.x + 5
        if evento.key == pygame.K_LEFT:
            jogador.x = jogador.x - 5
    pass
def movimentar_bola():
    pass


blocos = criar_blocos(qtd_linhas, qtd_colunas)

while not fim_jogo:
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True
        movimentar_jogador(evento)
    #verifica a cada milissegundo:
    pygame.time.wait(1)
    pygame.display.flip()
pygame.quit()
