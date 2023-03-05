dia = 1mes = 30
ano = 365

idade = int(input())

qtdeAnos = idade // ano
restoAnos = idade % ano
qtdeMeses = restoAnos // mes
qtdeDias = restoAnos % mes

print(f"{qtdeAnos} ano(s)" + "\n" + f"{qtdeMeses} mes(es)" + "\n" + f"{qtdeDias} dia(s)")
