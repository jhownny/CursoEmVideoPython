# Desafio 074 - Crie um programa que vai 
# gerar cinco números aleatórios e 
# colocar em uma tupla.

# Depois disso, mostre a listagem de 
# números gerados e também indique o menor 
# e o maior valor que estão na tupla.

import random
cont = 0
l = []    
menor_n = 0
maior_n = 0
while cont < 5:
    aleatorio = random.randrange(1,100)
    if cont == 0:
        menor_n = aleatorio
        maior_n = aleatorio
    else:
        if aleatorio < menor_n:
            menor_n = aleatorio
        if aleatorio > maior_n:
            maior_n = aleatorio
    l.append(aleatorio)

    cont+=1
tupla = tuple(l)
print(f'A lista de numeros digitados foi {tupla};\nO menor número foi o {menor_n};\nO maior número foi o {maior_n}. ')