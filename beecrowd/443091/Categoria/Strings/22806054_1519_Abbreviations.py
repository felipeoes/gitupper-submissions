entrada = ""linhas = []
palavrasAbreviadas = []
listaAbreviacoes = []
significadosAbreviacoes = []
letrasUsadas = []

while(entrada != "."):
    entrada = input()
    linhas.append(entrada)

def deveAbreviar2(palavra: str):
    for palavraAbreviada in palavrasAbreviadas:
        if(palavraAbreviada[0] == palavra[0]):
            if(len(palavraAbreviada) < len(palavra)):
                return False  # palavra já abreviada é menor, então sigo com a abreviação da nova palavra e retorno palavraAbreviada para remoção da Lista
            
            elif(len(palavraAbreviada) > len(palavra)):
                return  palavraAbreviada# palavra já abreviada é maior, então não devo abreviar
            
def deveAbreviar(palavra: str):
    for palavraAbreviada in palavrasAbreviadas:
        if(palavraAbreviada[0] == palavra[0]):
            if(len(palavraAbreviada) > len(palavra)):
                return False  # palavra já abreviada é maior, então não devo abreviar
            elif(len(palavraAbreviada) < len(palavra)):
                return palavraAbreviada  # palavra já abreviada é menor, então sigo com a abreviação da nova palavra e retorno palavraAbreviada para remoção da Lista


def realizaAbreviacao(palavra: str):
    abreviacao = palavra[0] + '.'
    significado = abreviacao + " = " + palavra
    letrasUsadas.append(palavra[0])
    listaAbreviacoes.append(abreviacao)
    significadosAbreviacoes.append(significado)
    palavrasAbreviadas.append(palavra)


def realizaRemocaoAbreaviacao(palavra: str):
    qtdeRemovidos = 0
    abreviacao = palavra[0] + "."
    significado = abreviacao + " = " + palavra
    for i in range(len(significadosAbreviacoes)):
        if(significadosAbreviacoes[i] == significado):
            significadosAbreviacoes.remove(significadosAbreviacoes[i])
            index = listaAbreviacoes.index(abreviacao)
            try:
                while True:
                    listaAbreviacoes.remove(abreviacao)
                    listaAbreviacoes.insert(
                index, palavra)
                    
                    # listaAbreviacoes.remove(abreviacao)
            except ValueError:
                pass
            palavrasAbreviadas.remove(palavra)
            qtdeRemovidos += 1
    return qtdeRemovidos


def abreviadorPalavras(linha: str):
    contagemAbreviacao = 0
    palavras = linha.split(" ")

    for palavra in palavras:
        if(len(palavra) > 2 and not(palavra in palavrasAbreviadas)):
            if(palavra[0] in letrasUsadas):
                palavraAntiga = deveAbreviar(palavra)
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

def abreviadorPalavras2(linha: str):
    contagemAbreviacao = 0
    palavras = linha.split(" ")

    for palavra in palavras:
        if(len(palavra) > 2 and not(palavra in palavrasAbreviadas)):
            if(palavra[0] in letrasUsadas):
                palavraAntiga = deveAbreviar2(palavra)
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

def comparaAbreviacoes(abreviacao0: str, abreviacao1: str):
    if(len(abreviacao0.strip()) > len(abreviacao1.strip())):
        return True
    return False

listaSignificado0 = []
listaSignificado1 = []
contagemAbreviacao0 = 0
contagemAbreviacao1 = 0
for i in range(len(linhas) - 1):
    contagemAbreviacao0 = abreviadorPalavras(linhas[i])
    abreviacoes0 = ' '.join(listaAbreviacoes)
    listaSignificado0 = significadosAbreviacoes
    # print(abreviacoes)
    # print(contagemAbreviacao)
    # imprimeSignificado(significadosAbreviacoes)
    palavrasAbreviadas = []
    letrasUsadas = []
    significadosAbreviacoes = []
    listaAbreviacoes = []
    
    contagemAbreviacao1 = abreviadorPalavras2(linhas[i])
    abreviacoes1 = ' '.join(listaAbreviacoes)
    listaSignificado1 = significadosAbreviacoes
    
    if(comparaAbreviacoes(abreviacoes0, abreviacoes1)):
        print(abreviacoes1)
        print(contagemAbreviacao1)
        imprimeSignificado(listaSignificado1)

    else:
        print(abreviacoes0)
        print(contagemAbreviacao0)
        imprimeSignificado(listaSignificado0)
    
    palavrasAbreviadas = []
    letrasUsadas = []
    significadosAbreviacoes = []
    listaAbreviacoes = []
