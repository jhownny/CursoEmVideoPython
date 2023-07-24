# Desafio 088 - Faça um programa que ajude um jogador 
# da MEGA SENA  a criar palpites. O programa vai perguntar 
# quantos jogos serão gerados e vai sortear 6 números entre 
# 1 e 60 para cadas jogo, cadastrando tudo em uma lista composta. 

import random

cont = 0
jogos = []

QuantGame = int(input('Digite quantos jogos deseja gerar: '))

while QuantGame > 0:
    jogos.append([])
    QuantGame-=1

    for l in range(6):
        a = random.randrange(1,60)
        jogos[cont].append(a)

    cont+=1

cont = 0
print('\nOs palpites dos jogos solicitados são esses:')

for MegaSena in jogos:
    print(f' {cont+1}° Jogo: {MegaSena}')
    cont+=1



