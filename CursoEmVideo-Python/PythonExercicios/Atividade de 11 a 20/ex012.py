# Desafio 012 - Faça um Algoritmo
# que leia o preço de um produto
# e mostre seu novo preço, com 5% de Desconto.

p = float(input('qual o preço do produto? '))
vd = (p*0.05)
vf = (p-vd)

print('este produto de R${} Reais está com o desconto de 5% que é equivalente a R${:1f} Reais'.format(p, vf))
