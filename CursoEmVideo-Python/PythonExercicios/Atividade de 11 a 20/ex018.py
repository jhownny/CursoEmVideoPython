
# Desafio 018 - Faça um programa que
# leia um ângulo qualquer e mostre na
# tela o valor do seno, cosseno e tangente
# desse ângulo.

# [import math] ou [from math import radians, sin, cos, tan]

import math

print('não fiz, não sabia por onde começar. Resolução do codigo a baixo:\n')

an = float(input('Digite o Ângulo que você deseja: '))
seno = math.sin(math.radians(an))
# seno = sin(radians(an))
print(f'O ângulo de {an} tem o SENO de {seno:.2f}')
cos = math.cos(math.radians(an))
# cos = cos(radians(an))
print(f'O ângulo de {an} tem o cosseno de {cos:.2f}')
tan = math.tan(math.radians(an))
# tan = tan(radians(an))
print(f'O ângulo de {an} tem a tangente de {tan:.2f} ')

# Segundo python.org:
# math.sin(x): Retorna o seno de x radianos.
# math.radians(x): Converte o ângulo x de graus para radianos.
# math.tan(x): Retorna o tangente de x radianos.
# math.cos(x): Retorna o cosseno de x radianos.
# obs:ajuda pra caramba em! saquei tudo...(ironia)
