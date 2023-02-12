
# Desafio 024 - Crie um programa que
# leia o nome de uma cidade e diga
# se ela começa ou não com o nome "SANTO".

cid = str(input('digite o nome da sua cidade\n: '))
# var: declara em que posição se encontra a palavra sendo "0" a primeira e -1 quando não tem.
mcid = cid.upper()
var = mcid.find('SANTO')

if var == 0:
    print(f'O nome da sua cidade, a cidade {cid}, começa com Santo!')

else:
    print(f'O nome da sua cidade, a cidade {cid}, não começa com Santo.')
