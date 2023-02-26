# Desafio 031 - Desenvolva um programa que
# pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 para
# viagens mais longas.

dis = float(input('Quantos quilometros essa viagem vai dar?\n:'))

if dis <= 200.0:
    print(f'OK, com {dis}Km você ira pagar de passagem: R${dis*0.50:.2f}')
else:
    print(f'OK, com {dis}Km você ira pagar de passagem: R${dis*0.45:.2f}')