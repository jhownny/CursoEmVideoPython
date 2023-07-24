# Desafio 017 - Faça um programa que
# leia o comprimento de cateto oposto
# e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento
# da hipotenusa.

import math

co = int(input('me diga o valor do cateto oposto:'))
ca = int (input('me diga o valor do cateto adjacente:'))
x = (co ** 2) + (ca ** 2)
h = math.sqrt(x)

print(f'{h:.0f}')