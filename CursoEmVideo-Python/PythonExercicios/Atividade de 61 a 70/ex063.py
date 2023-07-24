# Desafio 063 - Escreva um programa que leia um
# número n inteiro qualquer e mostre na tela
# os n primeiros elementos de uma Sequência de Fibonacci.
#
#Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input("Digite o número de elementos da sequência de Fibonacci que deseja ver: "))

if n <= 0:
    print("Digite um número inteiro positivo maior que zero.")
else:
    sequence = [0, 1]
    if n == 1:
        print("Sequência de Fibonacci com 1 elemento:")
        print(sequence[0])
    else:
        print("Sequência de Fibonacci com", n, "elementos:")
        print(sequence[0], end=" -> ")
        for i in range(1, n - 1):
            next_number = sequence[i] + sequence[i - 1]
            sequence.append(next_number)
            print(next_number, end=" -> ")
        print(sequence[n - 1])