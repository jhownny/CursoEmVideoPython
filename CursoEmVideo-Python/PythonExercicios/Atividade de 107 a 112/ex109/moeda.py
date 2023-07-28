# Desafio 109 - Modifique as funções que foram criadas no 
# desafio 107 para que elas aceitem um parâmetro a mais, informando 
# se o valor retornado por elas vai ser ou não formatado pela 
# função moeda(), desenvolvida no desafio 108.

def metade(num, form = True):
    num/=2
    if form == True:
        return (f'R${num:.2f}') 
    else:
        return num


def dobro(num, form = True): 
    num*=2
    if form == True:
        return (f'R${num:.2f}')
    else:
        num*=2
        return num


def aumentando(num, taxa, form = True):
    res = num + (num*taxa/100)
    if form == True:
        return (f'R${res:.2f}')
    else:
        return res


def diminuindo(num,taxa, form = True):
    res = num - (num*taxa/100)
    if form == True:
        return (f'R${res:.2f}')
    else:
        return res


def moeda(num):
    return (f'R${num:.2f}')


#Ex:

# from ex109 import moeda

#p = float(input('digite o preço: R$'))              # [O Valor bolleano vai indicar se ele vai ou não ser formatado.]
#print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')