# Desafio 029 - Escreva um programa que
# leia a velocidade de um carro.
#
# Se ele ultrapassar 80Km/h, mostre
# uma mensagem dizendo que ele foi multado.
#
# A multa vai custar R$7,00
# por cada Km acima do limite.

velocidade = float(input('Por favor informe a velocidade que seu carro se encontra\n:'))
velomais = velocidade - 80

if velocidade <= 80.0:
    print(f'Parece que com {velocidade}Km, você não ultrapassou o limite de velocidade.')
else:
    print(f'Infelizmente você foi multado(a) com R${velomais*7.00:.2f}, '
          f'\npor estar {velocidade}Km acima da velocidade permitida.')