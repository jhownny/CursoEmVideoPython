# Desafio 086 - Crie um programa que crie uma matriz 
# de dimensão 3x3 e preencha com valores lidos pelo teclado.

# No final, mostre a matriz na tela, com a formatação correta.
cont = 0
m= [[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ]]
while cont < 9:
    num = int(input(f'Digite o {cont+1}° número: '))

    m[cont].append(num)

    cont+=1

print(f'\n{m[0]} \xA0 {m[1]} \xA0 {m[2]}')
print(f'{m[3]} \xA0 {m[4]} \xA0 {m[5]}')
print(f'{m[6]} \xA0 {m[7]} \xA0 {m[8]}\n')

# Assim que o resultado deve se apresentar:
#
#[ 1 ][ 2 ][ 3 ]
#[ 4 ][ 5 ][ 6 ]
#[ 7 ][ 8 ][ 9 ]
#
