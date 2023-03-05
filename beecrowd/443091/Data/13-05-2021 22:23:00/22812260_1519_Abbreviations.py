entrada = ""linhas = []
palavrasAbreviadas = []
listaAbreviacoes = []
significadosAbreviacoes = []
letrasUsadas = []
contagemPalavras = []
dicionarioPalavras = {}

while(entrada != "."):
    entrada = input()
    linhas.append(entrada)


def contaPalavras(linha: str):
    palavras = linha.split(" ")
    for palavra in palavras:
        dicionarioPalavras[palavra] = palavras.count(palavra)


def deveAbreviar(palavra: str, linha: str):
    for palavraAbreviada in palavrasAbreviadas:
        if(palavraAbreviada[0] == palavra[0]):
            contagemPalavra = dicionarioPalavras[palavra]
            contagemPalavraAbreviada = dicionarioPalavras[palavraAbreviada]
            totalCaracteresPalavraAbreviada = contagemPalavraAbreviada * \
                len(palavraAbreviada)
            totalCaracteresPalavra = contagemPalavra * len(palavra)
            qtdeVantagemPalavra = totalCaracteresPalavra - \
                (2 * contagemPalavra)
            qtdeVantagemPalavraAbreviada = totalCaracteresPalavraAbreviada - \
                (2 * contagemPalavraAbreviada)
            # if(len(palavraAbreviada) > len(palavra) and contagemPalavraAbreviada > contagemPalavra):
            #     return False  # palavra já abreviada é maior, então não devo abreviar
            # elif(len(palavraAbreviada) < len(palavra) and contagemPalavra >= contagemPalavraAbreviada):
            #     return palavraAbreviada  # palavra já abreviada é menor, então sigo com a abreviação da nova palavra e retorno palavraAbreviada para remoção da Lista
            # elif(contagemPalavra > 1 and contagemPalavraAbreviada > 1):
            #     if(totalCaracteresPalavraAbreviada < totalCaracteresPalavra):
            #         return palavraAbreviada
            # elif(contagemPalavra == 1 and contagemPalavraAbreviada > 1): # caso em que a primeira palavra abreviada é menor q a ultima (que é maior q a primeira)
            if(qtdeVantagemPalavra > qtdeVantagemPalavraAbreviada):
                return palavraAbreviada

    return False


def realizaAbreviacao(palavra: str):
    abreviacao = palavra[0] + '.'
    significado = abreviacao + " = " + palavra
    letrasUsadas.append(palavra[0])
    listaAbreviacoes.append(abreviacao)
    significadosAbreviacoes.append(significado)
    palavrasAbreviadas.append(palavra)


def realizaRemocaoAbreaviacao(palavra: str):
    global listaAbreviacoes
    qtdeRemovidos = 0
    abreviacao = palavra[0] + "."
    significado = abreviacao + " = " + palavra
    for significadoAbreviacao in significadosAbreviacoes:
        if(significadoAbreviacao == significado):
            significadosAbreviacoes.remove(significadoAbreviacao)
            listaAbreviacoes = [palavra if x ==
                                abreviacao else x for x in listaAbreviacoes]
            palavrasAbreviadas.remove(palavra)
            qtdeRemovidos += 1
    return qtdeRemovidos


def abreviadorPalavras(linha: str):
    contagemAbreviacao = 0
    palavras = linha.split(" ")

    for palavra in palavras:
        if(len(palavra) > 2 and not(palavra in palavrasAbreviadas)):
            if(palavra[0] in letrasUsadas):
                palavraAntiga = deveAbreviar(palavra, linha)
                if(palavraAntiga):
                    qtdeRemovidos = realizaRemocaoAbreaviacao(palavraAntiga)
                    contagemAbreviacao -= qtdeRemovidos
                else:
                    listaAbreviacoes.append(palavra)
                    continue
            realizaAbreviacao(palavra)
            contagemAbreviacao += 1
        elif(len(palavra) <= 2):
            listaAbreviacoes.append(palavra)
        else:  # palavra tem tamanho maior q 2 porém já foi abreviada
            abreviacao = palavra[0] + '.'
            listaAbreviacoes.append(abreviacao)
    return contagemAbreviacao


def imprimeSignificado(listaSignificados):
    listaSignificados.sort()
    for i in range(len(listaSignificados)):
        print(listaSignificados[i])


for i in range(len(linhas) - 1):
    contaPalavras(linhas[i])
    contagemAbreviacao0 = abreviadorPalavras(linhas[i])
    abreviacoes0 = " ".join(listaAbreviacoes)
    listaSignificado0 = significadosAbreviacoes
    print(abreviacoes0)
    print(contagemAbreviacao0)
    imprimeSignificado(listaSignificado0)

    palavrasAbreviadas = []
    letrasUsadas = []
    significadosAbreviacoes = []
    listaAbreviacoes = []
    contagemPalavras = []
    dicionarioPalavras = {}
