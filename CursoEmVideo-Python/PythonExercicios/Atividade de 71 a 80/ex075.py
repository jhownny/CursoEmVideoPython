# Desafio 078 - Faça um programa que leia 
# 5 valores numéricos e guarde-os em uma lista.

# No final, mostre quaal foi o maior e o menor 
# valor digitado e as suas respectivas posições na lista.

lista = []
cont = 0
menorN = 0
maiorN = 0
while True:
    numero = int(input(f'Digite o {cont+1}° numero: '))
    if cont == 0:
        maiorN = numero
        menorN = numero
    if numero < menorN:
        menorN = numero
    elif numero > maiorN:
        maiorN = numero
    cont+=1
    lista.append(numero)

    if cont == 5:
        break

print(f'O Maior Número é o {maiorN}, \nO Menor Número é o {menorN} \nE a Ordem de Colocação de Cada um é Essa: {lista}')
