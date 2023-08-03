# Desafio 038 - Escreva um programa que leia dois
# números inteiros e compare-os mostrando na tela
# uma mensagem:
#
# O primeiro valor é maior;
# O segundo valor é maior;
# Não existe valor maior, os dois são iguais.

n1 = int(input('Digite o \033[1;35mPrimeiro\033[m numero inteiro:'))
n2 = int(input('Digite o \033[1;31mSegundo\033[m numero inteiro:'))

if n1 > n2:
    print(f'\nO \033[1;35mPrimeiro\033[m número é maior que o \033[1;31Segundo\033[m. \n{n1} é maior que {n2}')
elif n2 > n1:
    print(f'\nO \033[1;31mSegundo\033[m número é maior que o \033[1;35mPrimeiro\033[m. \n{n2} é maior que {n1}')
else:
    print(f'\nNão existe valor maior, os dois são iguais. \n{n1} é igual a {n2}')
