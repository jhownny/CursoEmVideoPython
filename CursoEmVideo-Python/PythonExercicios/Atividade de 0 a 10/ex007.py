# Desafio 007 - Desenvolva um programa
# que leia as duas notas de um aluno,
# calcule e mostre a sua média.

n1 = int(input('Diga a primeira nota do aluno: '))
n2 = int(input('Diga a segunda nota do aluno: '))

print('O Aluno tendo tirado {} na primeira nota e {} na segunda, \nacabou que sua media foi de: {}'.format(n1, n2, (n1+n2)/2))
