
# Desafio 027 - Faça um programa
# que leia o nome completo de uma
# pessoa, mostrando em seguida o
# primeiro e o último nome separadamente.

n = str(input('Me diga seu nome\n: ')).strip()

nome = n.split()

print(f'O seu primeiro nome é {nome[0]}.')
print(f'Seu ultimo sobrenome é {nome[-1]}.')
