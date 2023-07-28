# Desafio 111 - Crie um pacote chamado utilidadesCev que 
# tenha dois módulos internos chamados moeda e dado.

# transfira todas as funções utilizadas nos desafios 
# 107,108 e 109 para o primeiro pacote e mantenha tudo funcionando.

def metade(num, form = True):
    num/=2
    if form == True:
        return (f'R${num:.2f}') 
    else:
        return num
    


#Ex:

# from ex111.utilidadesCeV import moeda

#p = float(input('digite o preço: R$'))
# moeda.resumo(p,80,35)