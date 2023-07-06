# Desafio 054 - Crie um programa que leia o
# ano de nascimento de sete pessoas.

# No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

# importação da função de data e hora.
from datetime import datetime

# chamada da função para definição da data presente
data_atual = datetime.now()
totalmaior = 0
totalmenor = 0

# Loop para cadastramento das pessoas com suas respectivas datas de nascimento.
for c in range(1, 8):
    ano = int(input(' Digite o ano de seu nascimento: '))

    # Idade é Igual ao ano Presente Menos o ano de Nascimento, por Exmplo:
    # 2004(Ano de Nascimento) - 2023(Ano Atual) = 19.
    idade = data_atual.year - ano

    # Se a Idade for maior ou igual a 18 ela será adicionada mais '1' a variavel "totalmaior".
    if idade >= 18:
        totalmaior += 1
    # Senão Será adicionada Menos '1' a variavel "totalmenor". 
    else:
        totalmenor += 1

# Resultado do Loop.
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade e {totalmenor} menores de idade')