# Desafio 034 - Escreva um programa
# que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
#
# Para salários superiores a
# R$1.250,00, calcule um aumento de 10%.
#
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Me diga seu salario, meu nobre\n:'))

if salario > 1.250:
    va = (salario * 0.10)
    vf = (salario + va)
    print(f'Você teve um aumento de 10% no seu salario: R${vf:.2f}')
else:
    va = (salario * 0.15)
    vf = (salario + va)
    print(f'Você teve um aumento de 15% no seu salario: R${vf:.2f}')


