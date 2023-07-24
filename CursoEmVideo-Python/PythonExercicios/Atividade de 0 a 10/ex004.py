# Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na 
# tela o seu tipo primitivo e todas as 
# informações possiveis sobre ele.

tipo = input('Digite algo: ')

if tipo.isalpha() == True:
    print(f'"{tipo}" defitnitivamente é uma string.')
elif tipo.isalnum() == True:
    print(f'"{tipo}" defitnitivamente é um número.')
if tipo.isupper() == True:
    print(f'E "{tipo}" defitnitivamente Tem ou é uma Letra Maiuscula.')
if tipo.islower() == True:
    print(f'E "{tipo}" defitnitivamente Tem ou é uma Letra Minuscula.')
