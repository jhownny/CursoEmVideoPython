# Desafio 066 - Crie um programa que leia 
# vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário 
# digitar o valor 999, que é a condição de parada. 
# No final, mostre qunatos números foram digitados e 
# qual foi a soma entre eles (desconsiderando o flag).

n = s = 0
while True:
    n = int(input('Digite os numeros para soma: '))
    if n == 999:
        break
    s+=n
print(f'A soma dos numros deu {s}!')