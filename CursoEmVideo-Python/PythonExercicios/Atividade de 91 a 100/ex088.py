# Desafio 091 - Crie um programa onde 4 jogadores 
# joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário. No final, 
# coloque esse dicionário em ordem, sabendo que o 
# vencedor tirou o maior número no dado.

import random
cont = 0
jogo = {}
dado = []
for c in range(0,3):
    a = random.randrange(1,6)
    jogo['jogador_indice'] = cont+1
    jogo['dado'] = a
    dado.append(jogo.copy())
    cont+=1

for i in dado:
    while True:
        print(f'O {i["jogador_indice"]}° jogador tirou {i["dado"]} no dado. ') 
        break
