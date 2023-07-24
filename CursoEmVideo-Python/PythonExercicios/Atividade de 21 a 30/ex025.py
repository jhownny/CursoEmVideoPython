# Desafio 025 - Crie um programa que
# leia o nome de uma pessoa e diga se
# ela tem "SILVA" no nome.

nome = str(input('Me diga seu nome completo\n: '))
mnome = nome.upper()
SeNome = 'SILVA' in mnome

if SeNome == True:
    print(f'Olá {nome}, Parece que seu nome contém "Silva"!')
else:
    print(f'Olá {nome}, Parece que seu nome não contém "Silva"!')
