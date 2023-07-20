# Desafio 099 - Faça um programa que tenha uma função 
# chamada maior(), que receba vários parâmetros com valores inteiros.

# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(lista):
    organizado = sorted(lista)
    print(f'O maior numeros da lista é o: {organizado[-1]}')
        

maior([67,2,84,110,30,6,35,8,94,20])