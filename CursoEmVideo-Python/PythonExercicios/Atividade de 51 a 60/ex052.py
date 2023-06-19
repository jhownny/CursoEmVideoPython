# Desafio 055 - Faça um programa que leia o
# peso de cinco pessoas. No final, mostre
# qual foi o maior e o menor peso lidos.

peso = 0
cont = 1
menor_peso = 0
maior_peso = 0

while cont <= 5:

    peso = float(input('Digite seu peso: '))

    if cont == 1:
        menor_peso = peso

    if peso < menor_peso:
        menor_peso = peso
    
    elif peso >= menor_peso:
        if peso >= maior_peso:
            maior_peso = peso
        
    cont+=1   

if maior_peso != menor_peso: 
    print(f'Menor peso: {menor_peso:.2f}, Maior peso: {maior_peso:.2f}.')

elif maior_peso == menor_peso:
    print(f'Os Pesos Digitados tem o Mesmo Valor: {maior_peso:.2f}')

# _____________________________ FEITO ________________________________________

menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input(f'peso da {p} pessoa'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
