# Desafio 037 - Escreva um programa que
# leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base
# de conversão:
#
# 1 para binário;
# 2 para octal;
# 3 para hexadecimal.

n = int(input('Digite um numero inteiro qualquer\n:'))
escolha = int(input('Me informe a conversão que deseja fazer\n'
                    '(1) para\033[1;35m Binário\033[m\n'
                    '(2) para\033[1;34m Octal\033[m\n'
                    '(3) para\033[1;33m Hexadecimal\033[m\n:'))

if escolha == 1:
    print(bin(n)[2::1])
elif escolha == 2:
    print(oct(n)[2::1])
elif escolha == 3:
    print(hex(n)[2::1])
else:
    print('---------------------------------------------------------------')
    print(f'\033[1;31m ERRO, dados informados não coincidem {escolha} não é um formato aceito! ')