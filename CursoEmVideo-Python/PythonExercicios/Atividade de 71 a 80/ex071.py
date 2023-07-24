# Desafio 071 - Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
# programa vai informar quantas células de cada valor serão entregues.
#
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Diga o Valor que Deseja Sacar: '))
cont_regresiva = 0
cont = 0
lista = []


v = valor
# Loop Responsavél por adicionar R$50 ao saque
while valor >= 50:
    cont_regresiva+=1
    valor = valor - 50
lista.insert(cont,cont_regresiva)
cont_regresiva = 0
cont+=1

# Loop Responsavél por adicionar R$20 ao saque
while valor >= 20 and valor <= 49:
    cont_regresiva+=1
    valor = valor - 20
lista.insert(cont,cont_regresiva)
cont_regresiva = 0
cont+=1

# Loop Responsavél por adicionar R$10 ao saque
while valor >= 10 and valor<= 19:
    cont_regresiva+=1
    valor = valor - 10
lista.insert(cont,cont_regresiva)
cont_regresiva = 0
cont+=1

# Loop Responsavél por adicionar R$1 ao saque
while valor >= 1 and valor <= 9:
    cont_regresiva+=1
    valor = valor - 1
lista.insert(cont,cont_regresiva)
cont_regresiva = 0


print(f'\nCom o saque de R${v:.2f} o caixa irá te entregar:\n{lista[0]} nota(s) de R$50.00, \n{lista[1]} nota(s) de R$20.00, \n{lista[2]} nota(s) de R$10.00, \n{lista[3]} nota(s) de R$1.00.')

# Ultimo exercicio do capitulo 15