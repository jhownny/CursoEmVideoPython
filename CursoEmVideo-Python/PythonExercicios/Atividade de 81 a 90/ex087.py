# Desafio 087 - Aprimore o desafio anterior, mostrando no final:

# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
maior = 0
cont = 0
l_par = []
m= [[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ]]
while cont < 9:
    num = int(input(f'Digite o {cont+1}° número: '))

    m[cont].append(num)
    if num%2==0:
        l_par.append(num)


    if (m[3]) > (m[4]) or (m[3]) > (m[5]):
        maior = m[3][0]  
    elif (m[4]) > (m[3]) or (m[4]) > (m[5]):
        maior = m[4][0]  
    elif (m[5]) > (m[4]) or (m[5]) > (m[3]):
        maior = m[5][0] 

    cont+=1

print(f'\n{m[0]} \xA0 {m[1]} \xA0 {m[2]}')
print(f'{m[3]} \xA0 {m[4]} \xA0 {m[5]}')
print(f'{m[6]} \xA0 {m[7]} \xA0 {m[8]}\n')

print(f'A soma de todos os valores({l_par}) pares digitados é: {sum(l_par)} ')
print(f'A soma dos valores presentes na tercera coluna é: {m[2][0] + m[5][0] + m[8][0]}')
print(f'O maior valor da segunda linha é o  número: {maior}')
