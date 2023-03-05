import sysfrom itertools import combinations

resp = []
resposta = []

def verificaLinhas(line: str):
    if(len(set(line)) == 1):
        resp1 = line[0]
        for i in range(1,len(line) + 1, 1):
            print(resp1 * i )
    else:    
        for p in range (1,len(line)+1):
            comb = combinations(line, p)
        #     for x in comb:
        #         if not (resp.__contains__(str(x).replace("(", "").replace(")", "").replace(",", "").replace("'", ""))):
        #             resp.append(str(x).replace("(", "").replace(")", "").replace(",", "").replace("'", ""))
        # toprint = sorted(resp)
        
        # for y in toprint:

        #     print(y.replace(" ", ""))
    
linhas = sys.stdin.read().strip().split('\n')

for l in linhas:
    verificaLinhas(l)
    
    print()
    resp.clear()
    resposta.clear()
    
