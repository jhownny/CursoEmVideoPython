# Desafio 081 - Crie um programa que vai ler vários 
# números e colocar em uma lista. 
# Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordednada de forma decrecente.
# C) Se o valor 5 foi digitado e está ou não na lista.

l = []
cont = 0
contnua = 0
while True:

    numero = int(input(f'Digite o {cont+1}° número: '))
    l.append(numero)
    if contnua == 9:
        pergunta = str.upper(input(f'Você já colocou {cont+1} números, deseja continuar? (S/N): '))
        contnua = 0

        if pergunta == 'N':
            break
    cont += 1
    contnua += 1

    
l.sort()
print(f'foram digitados {cont+1} numeros {l};\n')