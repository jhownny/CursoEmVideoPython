# Desafio 110 - Adicione ao módulo moeda.py criado nos desafios 
# anteriores, uma função chamada resumo(), que mostre na tela 
# algumas informações geradas pelas funções que já temos no módulo 
# criado até aqui.

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

# from ex110 import moeda

#p = float(input('digite o preço: R$'))
# moeda.resumo(p,80,35)

#-----------------------
#   RESUMO DO VALOR
#-----------------------
#Preço analizado:   R$500,00
#Dobro do preço:    R$1000,00
#MEtade do preço:   R$250,00
#80% de aumento:    R$900,00
#35% de Redução:    R$325,00
#-----------------------
