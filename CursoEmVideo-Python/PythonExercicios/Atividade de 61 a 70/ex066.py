# Desafio 069 - Crie um programa que eleia a idade e o sexo de várias pessoas. 
# A cada pessoa cadatrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
#
# A) Qunatas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

cont_idade = 0
cont_sexo = 0
cont_womanold = 0

while True:
    sexo = str.capitalize(input('Digite seu Sexo (Masculino ou Feminino): '))
    idade = int(input('Quantos anos você tem: '))
    print('====================================================')
    if idade > 18:
        cont_idade+=1
        if sexo == "Masculino":
            cont_sexo+=1
        elif sexo == "Feminino" and idade < 20:
            cont_womanold+=1
    else:
        if sexo == "Masculino":
            cont_sexo+=1
        elif sexo == "Feminino" and idade < 20:
            cont_womanold+=1
    Again = str.capitalize(input('Deseja continuar? \n:'))
    if Again == "Não":
        break
print('\n====================================================')
print(f'Teve {cont_idade} pessoa(s) com mais de 18 anos \n{cont_sexo} Homen(s) cadastrado(s) \n{cont_womanold} Mulher(es) com menos de 20 anos.')
print('====================================================\n')
