
# Desafio 022 - Crie um programa que
# leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras Maiúsculas.
# O nome com todas Minúsculas.
# Quantas Letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo\n: '))
nome2 = ';'.join(nome.split())
pnome, snome, tnome = nome2.split(";")

print(f'Seu nome com todas as letras Maiúsculas fica: {nome.upper()}')
print(f'Seu nome com todas as letras Minúsculas fica: {nome.lower()}')
print(f'O nome {nome} contém {len(nome)} letras')
print(f'{nome} seu primeiro nome {pnome} tem {len(pnome)} caracteres')
