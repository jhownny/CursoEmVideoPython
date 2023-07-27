# Desafio 108 - Adapite o código do desafio 107, criando uma 
# função adicional chamada moeda() que consiga mostrar os valores 
# como um valor monetário formado.

def metade(num):
    num/=2
    return num 


def dobro(num): 
    num*=2
    return num


def aumentando(num,taxa):
    return num + (num*taxa/100)


def diminuindo(num,taxa):
    return num - (num*taxa/100)


def moeda(num):
    return (f'R${num:.2f}')


#Ex:

# from ex108import moeda

#p = float(input('digite o preço: R$'))
#print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
