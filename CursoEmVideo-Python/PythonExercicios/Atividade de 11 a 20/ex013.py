# Desafio 013 - Faça um Algoritmo
# que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

s = float(input('Diga-me seu salario:R$'))
va = (s*0.15)
vf = (s+va)

print('R${}? Olha você recebeu 15% de aumento no seu salario UAU :R${}'.format(s, vf))
