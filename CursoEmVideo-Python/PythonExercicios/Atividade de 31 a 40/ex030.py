# Desafio 033 - Faça um programa
# que leia três números e mostre
# qual é o maior e qual é o menor.

num1 = int(input('me diga 3 numeros:'))
num2 = int(input(':'))
num3 = int(input(':'))

if num1 > num2 > num3:
    print(f'a ordem de procedencia do maior para o menor é {num1}, {num2}, {num3}.')
elif num2 > num3 > num1:
    print(f'a ordem de procedencia do maior para o menor é {num2}, {num3}, {num1}.')
elif num3 > num1 > num2:
    print(f'a ordem de procedencia do maior para o menor é {num3}, {num1}, {num2}.')
elif num2 > num1 > num3:
    print(f'a ordem de procedencia do maior para o menor é {num2}, {num1}, {num3}.')
elif num1 > num3 > num2:
    print(f'a ordem de procedencia do maior para o menor é {num1}, {num3}, {num2}.')
elif num3 > num2 > num1:
    print(f'a ordem de procedencia do maior para o menor é {num3}, {num2}, {num1}.')