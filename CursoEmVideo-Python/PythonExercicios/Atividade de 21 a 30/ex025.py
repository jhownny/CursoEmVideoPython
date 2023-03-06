# Desafio 028 — Escreva um programa que
# faça o computador "pensar" num número
# inteiro entre 0 a 5 e peça para o utilizador
# tentar descobrir qual foi o número escolhido
# pelo computador.
#
# O programa deverá escrever na tela se o utilizador venceu ou perdeu.

import random
num = random.randrange(0, 5)
user = int(input('Diga um numero de 0 a 5\n:'))

if num == user:
    print(f'Olha só, você acertou! \nO numero que o computador sorteou foi o número: {num}')
else:
    print(f'Não, esse não era o numero que o computador "pensou". \nInclusive, o numero que ele "pensou" foi o {num} ')