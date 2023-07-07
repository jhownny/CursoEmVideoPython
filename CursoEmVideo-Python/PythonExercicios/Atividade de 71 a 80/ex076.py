# Desafio 079 - Crie um programa onde o usuário possa 
# digitar vários valores numéricos e cadastre-os em 
# uma lista. Caso o número já exista lá dentro, 
# ele não será adicionado. No final, serão exibidos 
# todos os valores únicos digitados, em ordem crescente.

l = []
cont = 0
contnua = 0
while True:

    numero = int(input(f'Digite o {cont+1}° numero: '))
    l.append(numero)

    if contnua == 9:
        pergunta = str.upper(input(f'Você já colocou {cont+1} números, deseja continuar? (S/N): '))
        contnua = 0

        if pergunta == 'N' or pergunta == 'NÃO':
            break
    cont += 1
    contnua += 1
    l.sort()


print(l)