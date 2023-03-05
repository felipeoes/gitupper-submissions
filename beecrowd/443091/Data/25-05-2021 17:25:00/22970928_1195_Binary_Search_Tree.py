import sys#sys.setrecursionlimit(10000)

#guardando todas as entradas (EOF) 
linhas = sys.stdin.read().strip().split('\n')

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
    # print(f"{raiz.chave}", end="")
    percursoPrefixo(raiz.filhoEsq)
    percursoPrefixo(raiz.filhoDir)    
    # return caracteres

#função de percurso infixo
infixo = []
def percursoInfixo(raiz):
    if raiz is None:
        return
    
    percursoInfixo(raiz.filhoEsq)
    infixo.append(raiz.chave)
    # print(f"{raiz.chave} ", end="")
    percursoInfixo(raiz.filhoDir)    

#função de percurso posfixo
posfixo = []
def percursoPosfixo(raiz):
    if raiz is None:
        return

    percursoPosfixo(raiz.filhoEsq)
    percursoPosfixo(raiz.filhoDir)
    # print(f"{raiz.chave} ", end="")
    posfixo.append(raiz.chave)            

nCasoDeTeste = 1
#iterando cada caso de teste (pulando linhas[0] que contem o numero de casos de teste) 
for i in range(1, len(linhas) - 1, 2):
    chavesTexto = linhas[i+1].split(" ")
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
    print("Pre.: ",end="")
    percursoPrefixo(arvore.raiz)
    print(*prefixo)

    #percurso infixo
    print("In..: ", end="")
    percursoInfixo(arvore.raiz)
    print(*infixo)

    #percurso posfixo
    print("Post: ",end="")
    percursoPosfixo(arvore.raiz)
    print(*posfixo)

    #quebra de linha entre os casos de teste
    if (i != len(linhas) - 2):
        print("\n")
        prefixo = []
        infixo = []
        posfixo = []
        

#apos o ultimo caso, pula uma linha
print()