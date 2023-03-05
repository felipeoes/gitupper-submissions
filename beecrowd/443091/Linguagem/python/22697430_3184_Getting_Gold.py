import syssys.setrecursionlimit(10000)


def buscaPosicaoInicial(mapa):
    global linhaInicial, colunaInicial
    for i in range(larguraMapa):
        for j in range(alturaMapa):
            if(mapa[i][j] == 'P'):
                linhaInicial = i
                colunaInicial = j
                break


def verificaArmadilha(mapa, linha, coluna):
    if(mapa[linha - 1][coluna] == 'T' or mapa[linha][coluna + 1] == 'T' or mapa[linha + 1][coluna] == 'T' or mapa[linha][coluna - 1] == 'T'):
        return True
    return False


def verificaPosicao(mapa, lin, col):
    if(mapa[lin][col] != '#' and mapa[lin][col] != '*'):
        return True
    return False


entrada = input().split(" ")
alturaMapa = int(entrada[0])
larguraMapa = int(entrada[1])
mapa = []
linhaInicial = 0
colunaInicial = 0
qtdeOuro = 0

for i in range(larguraMapa):
    linhaEntrada = input()
    linha = []
    for j in range(alturaMapa):
        linha.append(linhaEntrada[j])
    mapa.append(linha)


def procuraCaminho(mapa, lin, col):
    global qtdeOuro

    if(mapa[lin][col] == 'G'):
        qtdeOuro += 1

    if (not(verificaPosicao(mapa, lin, col))):
        return False

    mapa[lin][col] = '*'

    if (not(verificaArmadilha(mapa, lin, col)) and procuraCaminho(mapa, lin - 1, col)):  # cima
        return True

    elif (not(verificaArmadilha(mapa, lin, col)) and procuraCaminho(mapa, lin, col + 1)):  # direita
        return True

    elif (not(verificaArmadilha(mapa, lin, col)) and procuraCaminho(mapa, lin + 1, col)):  # baixo
        return True

    elif (not(verificaArmadilha(mapa, lin, col)) and procuraCaminho(mapa, lin, col - 1)):  # esquerda
        return True

    mapa[lin][col] = '.'
    return False


buscaPosicaoInicial(mapa)
procuraCaminho(mapa, linhaInicial, colunaInicial)
print(qtdeOuro)
