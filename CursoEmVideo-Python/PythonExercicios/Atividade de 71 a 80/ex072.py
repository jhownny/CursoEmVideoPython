# Desafio 072 - Crie um programa que tenha uma 
# tupla totalmente preenchida com uma contagem 
# por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo 
# teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)
escolha = int(input('Diga um número de 0 a 20: '))
print('---------------------------------------------------------')
for c in  range( escolha, tupla[21]):
    print(f'{c}')