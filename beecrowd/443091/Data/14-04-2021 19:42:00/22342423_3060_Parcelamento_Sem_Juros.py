# Pdrinho está implementando o sistema de controle de pagamentos parcelados de uma grande empresa de cartão de crédito digital. Os clientes podem parcelar as compras sem juros no cartão, em até 18 vezes. Quando o valor V da compra é divisível pelo número P de parcelas que o cliente escolhe, todas as parcelas terão o mesmo valor. Por exemplo, se o cliente comprar um livro de V = 30 reais em P = 6 vezes, então as parcelas terão valores: 5, 5, 5, 5, 5 e 5. Mas se o valor da compra não for divisível pelo número de parcelas será preciso fazer um ajuste, pois a empresa quer que todas as parcelas tenham sempre um valor inteiro e somem no total, claro, o valor exato da compra. O que Pedrinho decidiu foi distribuir o resto da divisão de V por P igualmente entre as parcelas iniciais. Por exemplo, se a compra for de V = 45 e o número de parcelas for P = 7, então as parcelas terão valores: 7, 7, 7, 6, 6, 6 e 6. Quer dizer, como o resto da divisão de 45 por 7 é 3, então as 3 parcelas iniciais devem ter valor um real maior do que as 4 parcelas finais. Você precisa ajudar Pedrinho e escrever um programa que, dado o valor da compra e o número de parcelas, imprima os valores de cada parcela.
valor = int(input())
parcelas = int(input())
# escreve alguma coisa ae gu p eu ver se aparece aq

if (valor >= 10 and valor <= 1000 and parcelas >= 2 and parcelas <= 18):

    # caso divisivel ele roda esse código, senão esse código é ignorado e ele roda tudo q tá dps do print(resultado)
    if (valor % parcelas == 0):
        resultado = (valor // parcelas)

        for i in range(parcelas):
            print(resultado)

    else:
        restoDiv = valor % parcelas  # resto da divisao inteira 1000 % 18 = 10
        # resultado da divisao inteira é 55 arrendodado
        divInteiraArred = (valor // parcelas)
        subtracao1 = parcelas - restoDiv  # numero de parcelas - resto da divisao -> 8
        mult = (parcelas - restoDiv) * divInteiraArred
        subtracao2 = valor - mult  # subtrai os 550 do valor total 1000 - 550 = 450
        # divide a subtracao2 pela subtracao1 pra achar o valor das 8 parcelas restantes = 56
        resultado1 = subtracao2 // restoDiv  # 1 resultado é 55 * 10 = 550
        resultado2 = subtracao2 // restoDiv

        for i in range(restoDiv):
            print(resultado1)
        for i in range(subtracao1):
            print(divInteiraArred)
