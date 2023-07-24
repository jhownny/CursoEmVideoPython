# Desafio 065 - Crie um programa que leia vários números
# inteiros pelo teclado. No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.

n1 = -1
soma = []
saida = 'S'
print('Olá, Bem vindo ao programa de soma.')

while saida != 'N': 

    for i in range(10):
        n1 = int(input(f'Digite o numero para a soma: '))
        soma.append(n1)
    saida = str(input('Deseja Continuar Inserindo Numeros? (S/N): ')).upper()


soma_total = sum(soma)


print(f'\nA soma dos numeros digitados foi: {soma_total}!')

# Final dos Exercicios 14