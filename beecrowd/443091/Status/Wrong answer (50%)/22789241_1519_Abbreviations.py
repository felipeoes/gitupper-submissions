linhas = []listaAbreviacoes = []
listaSignificados = []
contagemAbreviacao = 0
entrada = ""

# verificacao
letrasUsadas = []
palavrasAbreviadas = []

while(entrada != "."):
    entrada = input()
    linhas.append(entrada)

# True: abreviação ja foi usada
# False: abreviação não foi usada


def verificaAbrevPalavra(palavra):
    global letrasUsadas
    global contagemAbreviacao
    if len(letrasUsadas) == 0:

        letrasUsadas.append(palavra[0])
        palavrasAbreviadas.append(palavra)
        return False

    else:
        for i in range(len(letrasUsadas)):
            if (letrasUsadas[i] == palavra[0]):

                for elemento in palavrasAbreviadas:
                    if (elemento[0] == palavra[0]):

                        if(len(elemento) >= len(palavra)):
                            return True

                        else:
                            abreviacao = elemento[0] + "."
                            significado = abreviacao + " = " + elemento
                            palavrasAbreviadas.remove(elemento)
                            listaAbreviacoes.insert(
                                listaAbreviacoes.index(abreviacao), elemento)
                            listaAbreviacoes.remove(abreviacao)
                            listaSignificados.remove(significado)
                            palavrasAbreviadas.append(palavra)
                            contagemAbreviacao -= 1
                            return False

        letrasUsadas.append(palavra[0])
        palavrasAbreviadas.append(palavra)
        return False

def abreviador(linha: str):
    global listaAbreviacoes
    global contagemAbreviacao
    global listaSignificados
    listaAbreviacoes = []
    contagemAbreviacao = 0
    listaSignificados = []

    palavras = linha.split(" ")
    for palavra in palavras:
        if(len(palavra) > 2):
            if(not(verificaAbrevPalavra(palavra))):
                letraInicial = palavra[0]
                abreviacao = letraInicial + "."
                listaAbreviacoes.append(abreviacao)
                significado = abreviacao + " = " + palavra
                listaSignificados.append(significado)
                contagemAbreviacao += 1
        else:
            listaAbreviacoes.append(palavra)
    return contagemAbreviacao


def imprimeSignificado():
    global listaSignificados
    listaSignificados.sort()
    for i in range(len(listaSignificados)):
        print(listaSignificados[i])


for i in range(len(linhas) - 1):
    abreviador(linhas[i])
    print(' '.join(listaAbreviacoes))
    print(contagemAbreviacao)
    imprimeSignificado()
    letrasUsadas = []
    palavrasAbreviadas = []
