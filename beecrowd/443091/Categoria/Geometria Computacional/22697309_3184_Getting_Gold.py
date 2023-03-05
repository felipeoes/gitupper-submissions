def buscaPosicaoInicial(mapa):    for i in range(larguraMapa):
        for j in range(alturaMapa):
            if(mapa[i][j] == 'P'):
                setaPosicaoInicial(i, j)
                break


def setaPosicaoInicial(linInicial, colInicial):
    global linhaInicial, colunaInicial
    linhaInicial = linInicial
    colunaInicial = colInicial


def pegaOuro(mapa, linha, coluna):
    if(mapa[linha][coluna] == 'G'):
        return True
    return False


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

    if (pegaOuro(mapa, lin, col)):
        qtdeOuro += 1

    if (not(verificaPosicao(mapa, lin, col))):
        return False

    mapa[lin][col] = '*'
    # mapa[indiceCaminho] = lin
    # mapa[indiceCaminho + 1] = col
    # indiceCaminho += 2
    # mapa[0] = indiceCaminho

    if (not(verificaArmadilha(mapa, lin, col)) and procuraCaminho(mapa, lin - 1, col)):  # cima
        return True

    if (not(verificaArmadilha(mapa, lin, col )) and procuraCaminho(mapa, lin, col + 1)):  # direita
        return True

    if (not(verificaArmadilha(mapa, lin, col)) and procuraCaminho(mapa, lin + 1, col)):  # baixo
        return True

    if (not(verificaArmadilha(mapa, lin, col)) and procuraCaminho(mapa, lin, col - 1)):  # esquerda
        return True

    # if (verificaPosicao(mapa, lin - 1, col) and procuraCaminho(mapa, lin - 1, col)):  # cima
    #     return True

    # if (verificaPosicao(mapa, lin, col + 1) and procuraCaminho(mapa, lin, col + 1)):  # direita
    #     return True

    # if (verificaPosicao(mapa, lin + 1, col) and procuraCaminho(mapa, lin + 1, col)):  # baixo
    #     return True

    # if (verificaPosicao(mapa, lin, col - 1) and procuraCaminho(mapa, lin, col - 1)):  # esquerda
    #     return True

    mapa[lin][col] = '.'
    # path_index -= 2
    return False


buscaPosicaoInicial(mapa)
procuraCaminho(mapa, linhaInicial, colunaInicial)
print(qtdeOuro)
