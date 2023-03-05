# Desafio 046 - Faça um programa que mostre na
# tela uma contagem regressiva para o estouro
# de fogos de artifício, indo de 10 até 0, com
# uma pausa de 1 segundo entre eles.

# time = delay de equivalencia a segundos, com .sleep.

import time
import emoji

for f in range(10, 0, -1):
    print(f)
    time.sleep(1)
print(emoji.emojize(':collision:Feliz Ano Novo:collision:', language = 'alias'))
