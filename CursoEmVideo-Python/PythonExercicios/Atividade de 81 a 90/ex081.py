# Desafio 084 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

# A) Quantos pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cont = 0
# A variável "cont" vai me ajudar a contar a 
# quantidade de pessoas cadastradas assim ja 
# atendendo a requisição (A).

while True:

    # insersão de resultados nas variaveis "nome" e "peso".
    nome = str(input(f'Diga o nome da {cont+1}° pessoa: '))
    peso = float(input(f'Diga o peso da {cont+1}° pessoa: '))
  
    # Caminho para final do código.
    if cont%5 == 0:
        Again = str.upper(input('Deseja continuar? \n(S/n): '))
        if Again == 'NÃO' or Again == 'N':
            break

    cont+=1