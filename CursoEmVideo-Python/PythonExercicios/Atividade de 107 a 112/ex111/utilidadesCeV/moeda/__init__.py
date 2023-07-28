# Desafio 111 - Crie um pacote chamado utilidadesCev que 
# tenha dois módulos internos chamados moeda e dado.

# transfira todas as funções utilizadas nos desafios 
# 107,108 e 109 para o primeiro pacote e mantenha tudo funcionando.

def metade(num):
    num/=2
    return num


def dobro(num): 
    num*=2
    return num


def aumentando(num, taxa,):
    res = num + (num*taxa/100)
    return res


def diminuindo(num,taxa,):
    res = num - (num*taxa/100)
    return res


def moeda(num):
    return (f'R${num:.2f}')


def resumo(num,taxa,redutaxa):

    print('-' * 30)
    print('     \033[1mRESUMO DO VALOR\033[m')
    print('-' * 30)
    print(f'Preço analizado:    {moeda(num)}')
    print(f'Dobro do Preço:     {moeda(dobro(num))}')
    print(f'Metade do preço:    {moeda(metade(num))}')
    print(f'{taxa}% de aumento:     {moeda(aumentando(num,taxa))}')
    print(f'{redutaxa}% de redução:     {moeda(diminuindo(num,redutaxa))}')
    print('-' * 30)

#Ex:

# from ex111.utilidadesCeV import moeda

#p = float(input('digite o preço: R$'))
# moeda.resumo(p,80,35)