# Desafio 056 — Desenvolva um programa que
# leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
#
# - A média de idade do grupo;
# - Qual é o nome do homem mais velho;
# - Quantas mulheres têm menos de 20 anos.

cont = 1
Nhomem_velho = ""
homem_velho = 0

while cont <= 4 :

    nome = str.capitalize(input('\nDigite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str.capitalize(input(f'{nome}, Digite o sexo que você se Identifica(Feminio ou Masculino): '))    

    if cont == 1:
        soma_idade = idade
    else:
        soma_idade += idade

    if sexo == "Masculino" or sexo == "M":
    
        if cont == 1:
            homem_velho = idade
            Nhomem_velho = nome
        
        elif homem_velho < idade:
            homem_velho = idade
            Nhomem_velho = nome
    else:
        cont_mulher = 0
        if idade < 20:
            nome_mulher = nome
            cont_mulher+=1

    cont+=1
print(f'A media de Idade das pessoas Digitadas é de: {soma_idade/4:.0f} Anos; \nO homem mais velho se chama: {Nhomem_velho} - {homem_velho:.0f} anos; \nTem {cont_mulher} Mulher(es), {nome_mulher} com menos de 20 anos.')

# Ultimo exercicio do capitulo 13