numeroEntradas = int(input())listaLinhas = []
for k in range(numeroEntradas * 2):
    linha = input()
    listaLinhas.append(linha)

#estrutura do No
class No:
    '''atributos
    chave = 0
    filhoEsq = None
    filhoDir = None'''

    #inicializador do No
    def __init__(self, chave):
        self.chave = chave
        self.filhoEsq = None
        self.filhoDir = None

#estrutura da Arvore Binaria de Busca
class arvoreBinariaDeBusca:
    '''atributo
    raiz = None'''
    
    #inicializaor da Arvore (raiz)
    def __init__(self, chave):
        self.raiz = No(chave)

    #função recursiva de inserção 
    def inserirNo(self, raiz, chave):

        #No nulo = caso base
        if raiz is None:
            raiz = No(chave)

        #chave é menor que a chave da raiz: tenta inserir na esquerda
        elif (raiz.chave > chave):
            if (raiz.filhoEsq is None):
                raiz.filhoEsq = No(chave)

            else:
                self.inserirNo(raiz.filhoEsq, chave)

        #chave é maior que a chave da raiz: tenta inserir na direita
        else: 
            if (raiz.filhoDir is None):
                raiz.filhoDir = No(chave)

            else:    
                self.inserirNo(raiz.filhoDir, chave)               

#função de percurso prefixo
prefixo = []
def percursoPrefixo(raiz):
    if raiz is None:
        return

    prefixo.append(raiz.chave)
    percursoPrefixo(raiz.filhoDir)    

#função de percurso infixo
infixo = []
def percursoInfixo(raiz):
    if raiz is None:
        return
    
    percursoInfixo(raiz.filhoEsq)
    infixo.append(raiz.chave)
    percursoInfixo(raiz.filhoDir)    

#função de percurso posfixo
posfixo = []
def percursoPosfixo(raiz):
    if raiz is None:
        return

    percursoPosfixo(raiz.filhoEsq)
    percursoPosfixo(raiz.filhoDir)
    posfixo.append(raiz.chave)            

nCasoDeTeste = 1
#iterando cada caso de teste (pulando linhas[0] que contem o numero de casos de teste) 
for i in range(0, len(listaLinhas), 2):
    chavesTexto = listaLinhas[i+1].split(" ")
    arvore = None
    
    #montando a arvore de busca
    for j in range(len(chavesTexto)):
        #inicializando a arvore
        if (j == 0):
            #primeiro elemento é a raiz
            arvore = arvoreBinariaDeBusca(int(chavesTexto[0]))

        else:
            arvore.inserirNo(arvore.raiz, int(chavesTexto[j]))

    #print do caso
    print(f"Case {nCasoDeTeste}:")
    nCasoDeTeste += 1

    #percurso prefixo
    percursoPrefixo(arvore.raiz)
    print(f"Pre.:", *prefixo)

    #percurso infixo
    percursoInfixo(arvore.raiz)
    print(f"In..:", *infixo)

    #percurso posfixo
    percursoPosfixo(arvore.raiz)
    print(f"Post:", *posfixo)
    
    #quebra de linha entre os casos de teste
    if (i != len(listaLinhas) - 2):
        print()
        prefixo = []
        infixo = []
        posfixo = []