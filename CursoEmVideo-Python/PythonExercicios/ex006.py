
# Desafio 008 - Escreva um programa
# que leia um valor em metros e o exiba
# convertido em centimetros e milímetros.

m = int(input('Me diga o tamanho em metros que quer converter: '))
c = m*100
mi = m*1000

print('O Valor de {} metros convertidos em \ncentimetros é de {} e em \nmilímetros é {} '.format(m, c, mi))
