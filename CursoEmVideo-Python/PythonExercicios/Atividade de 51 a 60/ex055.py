# Desafio 055 - Faça um programa que leia o
# peso de cinco pessoas. No final, mostre
# qual foi o maior e o menor peso lidos.

peso = 0
cont = 0
menor_peso = 0
maior_peso = 0

# Enqunato a variável cont(Contador) for menor a 6 o codigo a dentro será executado.
while cont < 5:

    # Declaração da variável peso, que tem como parâmetro um valor float. 
    peso = float(input(f'Digite seu peso da {cont+1}° pessoa: '))

    # Se cont(Contador) for igual a 1 ele executará o codigo a dentro.
    if cont == 0:
        # o menor peso(menor_peso) é igual a o peso que acaba de ser digitado.
        menor_peso = peso

    # Se peso for menor que menor_peso ele executará o codigo a dentro.
    if peso < menor_peso:
        # o menor peso(menor_peso) é igual a o peso que acaba de ser digitado.
        menor_peso = peso
    
    # Senão se peso for maior ou igual a menor_peso ele executará o codigo a dentro.
    elif peso >= menor_peso:

        # Se peso for maior ou igual a menor_peso ele executará o codigo a dentro.
        if peso >= maior_peso:
            # maior_peso é igual a peso.
            maior_peso = peso

    # Adiciona uma contagem a mais na variavel cont.
    cont+=1   

# Se maior_peso for diferente de menor_peso ele executará o codigo a dentro.
if maior_peso != menor_peso: 
    # Mostrará O texto a baixo dentro das aspas simples.
    print(f'Menor peso: {menor_peso:.2f}, Maior peso: {maior_peso:.2f}.')

# Senão  se maior_peso for igual a menor_peso ele executará o codigo a dentro.
elif maior_peso == menor_peso:
    # Mostrará O texto a baixo dentro das aspas simples.
    print(f'Os Pesos Digitados tem o Mesmo Valor: {maior_peso:.2f}')

