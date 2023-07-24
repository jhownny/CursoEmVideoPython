# Desafio 082 - Crie um programa que vai ler 
# vários números e colocar em uma lista.

# Depois disso, crie duas listas extras que 
# vão conter apenas os valores pares e os valores 
# impares digitados, respectivamente.

# Ao final, mostre o conteúdo mostre o 
# conteúdo das três listas geradas.
lv = []
l_par = []
l_impar = []
cont = 0
while True:

    v = int(input(f'Digite o {cont+1}° número: '))
    lv.append(v)
    if v %2 == 0:
        l_par.append(v)
    else:
        l_impar.append(v)
    
    final = str.upper(input(f'Deseja continuar? [S/n]: '))
    if final == 'N' or final == 'NÃO':
        break

    cont+=1

print('~=' * 15)
print(f'Esses são os {cont+1} números que você digitou: {lv}')
print(f'Esses são os numeros pares digitados: {l_par}')
print(f'Esses são os numeros impares digitados: {l_impar}')
