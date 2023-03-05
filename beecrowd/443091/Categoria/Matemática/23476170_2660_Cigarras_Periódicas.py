import sysimport math

entrada = sys.stdin.read().strip().split('\n') # leitura da entrada
N = int(entrada[0].split(" ")[0])
L = int(entrada[0].split(" ")[1])

ciclos = [int(elemento) for elemento in entrada[1].split(" ")] # lista com os valores dos ciclos
visitados = {}  # dicionário contendo os respectivos mmc's dos ciclos já visitados

# a função calculaT recebe o limite L do enunciado e o mmcGeral, que é o resultado do mmc de todos os ciclos e realiza o mmc do atual mmcGeral com o iesimo numero, onde 2 <= i <= L.
# Todos os mmc's resultantes são adicionados no dicionário de visitados e ao final do algoritmo é recuperado o indice do mmc de maior valor, o qual representa o período que
# maximiza a quantidade de iterações.
def calculaT(L: int, mmcGeral: int):
    for i in range(2, L + 1, 1):  
        mmc = math.lcm(mmcGeral, i)
        
        if mmc == L:
            if not visitados:
                visitados.update({mmc:1})
            else:
                visitados.update({mmc: mmc})  
            return
            
        if not visitados:
            if i == 2:
                visitados.update({mmc: 1})
            else:
                visitados.update({mmc: i})
        if mmc < L and mmc > list(visitados)[-1]:
            visitados.update({mmc: i})


mmcGeral = 1
for i in range(len(ciclos)):
    mmcGeral = math.lcm(ciclos[i], mmcGeral)

calculaT(L, mmcGeral)
print(visitados[max(visitados)])