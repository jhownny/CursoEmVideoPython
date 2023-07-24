# Desafio 098 - Faça um programa que tenha uma função chamda contador(), 
#que receba três parâmetros:inicio, fim e passo e realize a contagem.

# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1;
# b) De 10 até 0, de 2 em 2;
# c) Uma contagem personalizada.

def contador(inicio,fim,passo):
    print('Contagem de 1 até 10, de 1 em 1:')
    for i in range(1,11,1):
        print(f' {i}', end=' ')
    print('\nContagem de 10 até 0, de 2 em 2:')
    for i in range(10,-1,-2):
        print(f'{i}', end=' ')
    print(f'\nContagem personalizada de {inicio} até {fim}, de {passo} em {passo}:')
    for p in range(inicio,fim,passo):
        print(f'{p}', end=' ')
    print(' ')

contador(5,20,2)