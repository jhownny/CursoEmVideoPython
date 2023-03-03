# Desafio 043 - Desenvolva uma lógica que
# leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de
# acordo com a tabela abaixo:
#
# Abaixo de 18.5:Abaixo do Peso;
# Entre 18.5 e 25:Peso ideal;
# 25 até 30:Sobrepeso;
# 30 até 40:Obesidade;
# Acima de 40:Obesidade Mórbida.

altura = float(input('Informe sua altura:'))
peso = float(input('Informe seu peso:'))
IMC = peso / (altura * altura)

if IMC < 18.5:
    print(f'\nAbaixo do Peso: {IMC:.2f}')

elif IMC >= 18.5 and IMC <= 25.0:
    print(f'\nPeso Ideal: {IMC:.2f}')

elif IMC >= 26 and IMC <= 30:
    print(f'\nSobrepeso: {IMC:.2f}')

elif IMC >= 31 and IMC <= 40:
    print(f'\nObesidade: {IMC:.2f}')

else:
    print(f'\nObesidade Morbida: {IMC:.2f}')
