# Desafio 051 - Desenvolva um programa que
# leia o primeiro termo e a ração de uma PA.
# No final, mostre os 10 primeiros
# termos dessa progressão.

an = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a Reação: '))
m = an + (10-1)*r

for c in range(an, m, r):
    print(f'{c} ', end='→ ')

print(' Final')



