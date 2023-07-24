# Desafio 075 - Desenvolva um programa que leia 
# quatro valores pelo teclado e guarde-os em 
# uma tupla. No final, mostre:

# A) Quantos vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

onde = []
l = []
cont_nove = 0
cont = 0

while cont < 4:
    num = int(input(f'Digite o {cont+1}° numero: '))
    cont+=1
    
    if num == 9:
        cont_nove+=1
        
    if num == 3:        
        onde.append(cont)
        
    if num %2 == 0:
        l.append(num)
        
aqui = tuple(onde)
n = tuple(l)
print(f'O número nove apareceu {cont_nove} vez(es); \nO primeiro numero 3 foi digtado na {aqui[0]}° posição; \nOs numeros pares digitados foram: {n}.')    