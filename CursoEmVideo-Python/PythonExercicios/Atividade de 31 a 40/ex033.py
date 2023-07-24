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

# Resolução proposta pelo guanabara:
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')


