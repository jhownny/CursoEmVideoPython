# Desafio 030 - Crie um programa que
# leia um número inteiro e mostre na
# tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um numero aleatório\n:'))

if num % 2 == 1:
    print(f'{num} é IMPAR.')
else:
    print(f'{num} é PAR.')
