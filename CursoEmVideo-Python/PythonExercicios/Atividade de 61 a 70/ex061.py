# Desafio 064 - Crie um programa que leia vários
# números inteiros pelo teclado. O programa só
# vai parar quando o usuário digitar o valor 999,
# que é a condição de para da. No final, mostre
# quantos números foram digitados e qual foi a
# soma entre eles (Desconsiderando o flag).

n1 = -1
soma = []
i = 0
print('Olá, Bem vindo ao programa de soma.')
print('Digite o numero "999" se quiser parar de fazer a soma dos valores.\n')
while n1 != 999: 


    n1 = int(input(f'Digite o {i+1}° numero para a soma: '))
    i = i+1
    soma.append(n1)


soma_total = sum(soma)
quant = len(soma)

print(f'\nVocê digitou {quant} numero(s) e a soma dele(s) é de {soma_total}!')