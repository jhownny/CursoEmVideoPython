# Desafio 061 — Refaça o DESAFIO 051
# lendo o primeiro termo e a razão de
# uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

an = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a Reação: '))
m = an + (10-1)*r
cont = 0

while an != m:
    print('{}'.format(), end='→')
    cont += 1