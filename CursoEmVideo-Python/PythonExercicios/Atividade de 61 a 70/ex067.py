# Desafio 067 - Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitados pelo usuári. O programa será 
# interronpido qunado o número solicitado for negativo.


while True:
    n = int(input('Digite um numero para tabuada: '))

    if n <= 0:
        break
    print('==========================================================')
    print(f'\n{n} X 1 = {n*1} \n{n} X 2 = {n*2} \n{n} X 3 = {n*3} \n{n} X 4 = {n*4} \n{n} X 5 = {n*5} \n{n} X 6 = {n*6} \n{n} X 7 = {n*7} \n{n} X 8 = {n*8} \n{n} X 9 = {n*9} \n{n} X 10 = {n*10}')
    print('\n==========================================================')

print(f'\n você digitou {n}? Então é isso que tem pra hoje. \n Tchau!')
