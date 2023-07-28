# Desafio 107 - Crie um módulo chamado moeda.py que 
# tenha as funções incorporadas aumentanto(), diminuindo(), dobro() e metade().

# faça também um programa que importe esse módulo e use algumas dessa funções.

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

    
#Ex:

# from ex107 import moeda

#p = float(input('digite o preço: R$'))
#print(f'A metade de {p} é {moeda.metade(p)}')