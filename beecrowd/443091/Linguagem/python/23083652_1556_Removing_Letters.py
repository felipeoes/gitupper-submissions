import sys
sys.setrecursionlimit(1000)

from itertools import permutations

def verificaLinhas(line: str):
        permutacoes = [''.join(p) for p in permutations(line)]
        print(permutacoes)


linhas = sys.stdin.read().strip().split('\n')

for l in linhas:
    verificaLinhas(l)