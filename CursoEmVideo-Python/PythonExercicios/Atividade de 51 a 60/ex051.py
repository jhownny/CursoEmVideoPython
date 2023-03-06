# Desafio 054 - Crie um programa que leia o
# ano de nascimento de sete pessoas.
#
# No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.
from datetime import datetime
data_atual = datetime.now()
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    ano = int(input(' Digite o ano de seu nascimento: '))
    idade = data_atual.year - ano
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade e {totalmenor} menores de idade')