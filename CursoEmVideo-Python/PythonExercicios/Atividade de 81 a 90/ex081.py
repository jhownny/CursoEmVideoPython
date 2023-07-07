# Desafio 084 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

# A) Quantos pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cont = 0
# A variável "cont" vai me ajudar a contar a 
# quantidade de pessoas cadastradas assim ja 
# atendendo a requisição (A).

peso_anterior = 0
l_map = []
l_mep = []
while True:

    # insersão de resultados nas variaveis "nome" e "peso".
    nome = str(input(f'Diga o nome da {cont+1}° pessoa: '))
    peso = float(input(f'Diga o peso da {cont+1}° pessoa: '))
    
    if cont == 0:
        peso_anterior = peso
        l_mep.append(peso)
    elif peso > peso_anterior:
        l_map.append(peso)
        peso_anterior = peso
    elif peso < peso_anterior:
        l_mep.append(peso)
        peso_anterior = peso

    # Caminho para final do código.
    Again = str.upper(input('Deseja continuar? \n(S/n): '))
    if Again == 'NÃO' or Again == 'N':
        break

    cont+=1
print('~=' * 21)
print(f'Foram cadastradas {cont+1} pessoas; \nAs mais pessadas: {l_map:.2f};\nAs mais leves: {l_mep:.2f}.')