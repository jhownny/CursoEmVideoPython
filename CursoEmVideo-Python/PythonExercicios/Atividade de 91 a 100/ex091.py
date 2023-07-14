# Desafio 094 - Crie um programa que leia nome, 
# sexo e idade de várias pessoas, guardando os dados 
# de cada pessoa em um dicionário e todos os dicionários 
# em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

cont = int(0)
pessoas = dict()
l_pessoas = list()

# Neste loop, pedimos parar o usuario colocar os valores no campos.  
while True:

    # Assim que digitados os valores vão para dentro dos respectivos dicionarios.
    pessoas['nome'] = str.title(input('Digite seu nome: '))
    pessoas['sexo'] = str.upper(input('Digite seu sexo [M/F]: '))
    pessoas['idade'] = int(input('Digite sua idade: '))
    l_pessoas.append(pessoas.copy())

    # Ponto de parada do loop caso o usuario digite "n" ou "não".
    parada = str.upper(input('Deseja Cadastrar mais pessoas? [S/n]: '))
    if parada == 'N' or parada == 'NÃO':
        break

# Neste loop, entro dentro da lista que se encontra os dicionarios. 
for i in l_pessoas:
    # Neste loop, faço a soma das idades cadastradas em cada dicionario. 
    while True:
        if cont == 0:
            anterior = i['idade']
        elif cont == 1:
            soma = anterior + i['idade']
        else:
            soma = soma + i['idade']
        cont+=1
        break

print( '-~'*30)

print(f'Foram cadastradas {len(l_pessoas)} pessoas;')
print(f'A media de idade das {len(l_pessoas)} pessoas Cadastradas é de {(soma/len(l_pessoas)):.0f} anos;')
print('Os nomes das mulheres cadastradas são: ', end='')

# Neste loop, entro dentro da lista que se encontra os dicionarios. 
for f in l_pessoas:
    # Neste loop, verifico se à o sexo "F" para que contabilize os nomes.  
    while True:
        if f['sexo'] == 'F':
            print(f'{f["nome"]},', end=' ')
        break
print(';')

# Neste loop, entro dentro da lista que se encontra os dicionarios. 
for p in l_pessoas:
    # Neste loop, verifico se a idade que tem dentro do campo idade dos dicionario é maior que a soma das idades dividido pela quantidade de dicionarios.
    while True:
        if p['idade'] > (soma/len(l_pessoas)):
            print(f'{p["nome"]},',end=' ')
        break

print('tem a idade acima da média.')
