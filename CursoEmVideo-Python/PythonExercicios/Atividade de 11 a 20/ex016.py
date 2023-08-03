# Desafio 016 - Crie um programa que leia
# um número Real qualquer
# pelo teclado e mostre na
# tela a sua porção inteira.

import math
nun = float(input('digite um numero: '))

print(f'O número {nun} tem como parte inteira {math.ceil(nun)}')
