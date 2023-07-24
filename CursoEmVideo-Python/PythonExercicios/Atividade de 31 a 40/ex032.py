# desafio 032 - Faça um programa que
# leia um ano qualquer e mostre se
# ele é BISSEXTO.

ano = int(input('Me diga o ano: '))

if ano % 4 == 0:
    print(f'{ano} é um ano BISSEXTO.')
else:
    print(f'{ano} não é umm ano BISSEXTO.')
