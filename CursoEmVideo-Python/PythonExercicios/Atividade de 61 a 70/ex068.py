# Desafio 068 - Faça um programa que jogue Par ou Impar com o computador. 
# O jogo só será Interrompido quando o Jogador PERDER, mostranto o total de 
# vitórias consecutivas que ele conquistou no final do jogo.

import random

cont = 0
n_computer = 0
n_jogador = 0

print('\nNeste jogo você jogara Impar ou Par (de 0 a 100) com a Maquina, Assim que você perder será contabilizado suas vitórias. \nBoa Sorte e Bom jogo! >:D ')
ParImpar = str.upper(input('\nEscolha entre Par ou Ipar: '))

print('=============================================')

if ParImpar == "PAR":
    print('\nOK! Você escolheu PAR. Vamos Comecar:\n')
else:
    print('\nOK! Você escolheu IMPAR. Vamos Comecar:\n')

while True:

    if ParImpar == "PAR":
        n_jogador = int(input('Escolha um número: '))
        n_computer = random.randrange(1 , 100)
        nun_final = n_jogador + n_computer
        if nun_final % 2 == 0:
            print(f'Você escolheu o número ({n_jogador}) e o Computador ({n_computer}) o resultado com a soma é Par!')
            cont+=1
        else:        
            print(f'\nVocê escolheu o número ({n_jogador}) e o Computador ({n_computer}) o resultado com a soma é Impar!')
            break
    elif ParImpar == "IMPAR":     

        n_jogador = int(input('Escolha um número: '))
        n_computer = random.randrange(1 , 100)
        nun_final = n_jogador + n_computer
        if nun_final % 2 == 0:
            print(f'\nVocê escolheu o número ({n_jogador}) e o Computador ({n_computer}) o resultado com a soma é Par!')
            break
        cont+=1
        print(f'Você escolheu o número ({n_jogador}) e o Computador ({n_computer}) o resultado com a soma é Impar!')


print(f'\nParece que dessa vez você perdeu, mas Pelo menos Ganhou {cont} Vezes! >:D')