# Desafio 059 — Crie um programa que
# leia dois valores e mostre um menu na tela:
#
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
#
# O seu programa deverá realizar
# a operação solicitada em cada caso.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
menu = 0

while menu != 5:
    menu = int(input('\n[1] somar'
                     '\n[2] multiplicar'
                     '\n[3] maior'
                     '\n[4] novos números'
                     '\n[5] sair do programa'
                     '\nDigite a operação desejada:'))
    if menu == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif menu == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'O maior numero entre {n1} e {n2} é: {n1}')
        elif n1 < n2:
            print(f'O maior numero entre {n1} e {n2} é: {n2}')
        else:
            print(f'{n1} e {n2} são iguais')
    elif menu == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo número: '))
    elif menu == 5:
        print('\nValeu, tenha um Bom Dia!')
    else:
        print(f'\nO Número {menu} não está na lista.')
