# Desafio 060 — Faça um programa que leia um número qualquer e mostre o seu fatorial.
#
#Ex:
#5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Digite um numero: '))
s = n
while s != 0:

    print('{}'.format(s), end=' x ')
    s -= 1
print(s * n)


