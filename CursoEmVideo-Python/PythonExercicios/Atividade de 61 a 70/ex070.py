# Desafio 070 - Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar. 
# No final, mostre:
#
# A) Qual é o total gasto na compra. 
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

l_precoTotal = []
cont_caro = 0
precomenor = 0
produtobarato = " "
cont = 0

while True:

    produto = str.capitalize(input('Digite nome do produto: '))
    preco = float(input(f'Digite o preço do {produto}: '))

    if cont == 0:
        precomenor = preco
        produtobarato = produto

    if preco > 1000:
        cont_caro+=1

    l_precoTotal.append(preco)
    precototal = sum(l_precoTotal)

    if preco < precomenor:
        precomenor = preco
        produtobarato = produto

    Again = str.capitalize(input('Deseja continuar? \n:'))
    cont+=1
    if Again == "Não":
        break

print('\n====================================================')
print(f'O Total da Compra deu: R${precototal:.2f}; \nTeve {cont_caro} Produtos com mais de R$1000,00; \nO produto mais barato foi o {produtobarato} que Custou R${precomenor:.2f}.')
print('====================================================\n')





