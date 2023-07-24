# Desafio 045 - Crie um programa que faça
# o computador jogar Jokenpô com você.

import random

escolha = str(input('Escolha entre pedra, papel e tesoura:'))
jokenpo = escolha.capitalize()

escolhaPC = 'Pedra', 'Papel', 'Tesoura'
jokenpoPC = random.choice(escolhaPC)

if jokenpoPC == jokenpo:
    print(f'\033[1;33mEmpatou\033[m! O resultado foi \033[1;34m{jokenpoPC}\033[m contra \033[1;34m{jokenpo}\033[m.')

elif jokenpoPC == 'Pedra' and jokenpo == 'Papel' or jokenpoPC == 'Tesoura' and jokenpo == 'Pedra' or jokenpoPC == 'Papel' and jokenpo == 'Tesoura':
    print(f'Você \033[1;32mGanhou\033[m! O resultado foi \033[1;35m{jokenpoPC}\033[m contra \033[1;34m{jokenpo}\033[m. ')

elif jokenpo == 'Pedra' and jokenpoPC == 'Papel' or jokenpo == 'Tesoura' and jokenpoPC == 'Pedra' or jokenpo == 'Papel' and jokenpoPC == 'Tesoura':
    print(f'Você \033[1;31mPerdeu\033[m! O resultado foi \033[1;34m{jokenpoPC}\033[m contra \033[1;35m{jokenpo}\033[m.')

else:
    print(f'Tem que ser Pedra, Papel ou Tesoura. Você escreveu: \033[4;31m{jokenpo}\033[m.')
# ultima atividade do capitulo 12

