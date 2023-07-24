# Desafio 085 - Crie um programa onde o usuário possa 
# digitar sete valores numéricos e cadastre-os em uma 
# lista única que mantenha separados os valores pares 
# e impares. No final, mostre os valores pares e 
# impares em ordem crescente.

cont = 0 
l = [[],[]]
while cont < 7:
    num = int(input(f'Digite o {cont+1}° numero: '))
    if num%2 == 0:
        l[0].append(num)
    else:
        l[1].append(num)
    cont+=1

l[1].sort()
l[0].sort()
tamanho0 = len(l[0])
tamanho1 = len(l[1])

print(f'Dos {cont} números digitados, {tamanho0}({l[0]}) são pares e  {tamanho1}({l[1]}) são impares.')