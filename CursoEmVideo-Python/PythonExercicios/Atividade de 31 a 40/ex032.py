# Desafio 035 - Desenvolva um programa que
# leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.

#funcionamento basico:
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

# a + b < c
# a + c < b
# b + c < c

reta1 = int(input('Me informe as três medidas das retas\n:'))
reta2 = int(input(':'))
reta3 = int(input(':'))

if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    print('Fecha um triângulo em meu querido!')
else:
    print('fechou não, meu bom')

# Ultimo exercicio do cap 10
