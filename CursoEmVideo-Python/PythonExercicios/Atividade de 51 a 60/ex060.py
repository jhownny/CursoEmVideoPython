# Desafio 060 — Faça um programa que leia um número qualquer e mostre o seu fatorial.
#
# Ex:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Digite um numero: '))
if n < 0:
    print("O fatorial não está definido para números negativos.")
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i

    print(f"{n}! = {fatorial}")


