# Desafio 010 - Crie um programa
# que leia quanto dinheiro uma
# pessoa tem na carteira e mostre
# quantos Dólares ela pode comprar.

c = float(input('me diga quantos real tem ai fi: '))
d = float(0.19)

print('parece que os R${} Reais que tem na sua carteira equivale a ${} Dolares'.format(c, c * d))