# Desafio 039 - Faça um programa que leia o ano de
# nascimento de um jovem e informe, de acordo com sua idade:
#
# Se ele ainda vai se alistar ao serviço militar.
# se é a hora de se alistar.
# Se já passou do tempo do alistamento.
#
# Seu programa também deverá mostrar o
# tempo que falto ou que passou do prazo.

from datetime import datetime

data_atual = datetime.now()
ano = int(input('Informe o ano de seu nascimento:'))
idade = data_atual.year - ano

if idade >= 19:
    print(f'Ja passou do tempo de se alistar! Parece que era para você ter se alistado a {idade-18} anos')
elif idade <= 17:
    print(f'Você ainda vai se alistar! Falta {(idade+18)-18} anos para você se alistar.')
else:
    print('Parece que você já pode se alistar!')
