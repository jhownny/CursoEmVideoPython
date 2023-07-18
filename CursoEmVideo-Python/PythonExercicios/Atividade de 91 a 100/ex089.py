# Desafio 092 - Crie um programa que leia nome, ano de 
# nascimento e carteira de trabalho e cadastre-os 
# (com idade) em um dicionário se por acaso a CTPS for 
# difrrente de ZERO, o dicionário receberá também o ano 
# de contratação e o salário, com qunatos anos a pessoa 
# vai se aposentar. 

nome =str(input('Digite seu nome'))
idade =int(input('Digite o ano de seu nascimento'))
CT = int(input('Digite a carteira de trabalho'))

#Ex:
# Nome: Jhonta
# Ano de Nascimento: 2004
# Carteira de Trabalho (0 não tem): 1234
# Ano de Contratação: 2020
# Salário: R$1000

# print('-=' * 20)

#{'nome':'Jhonata', 'idade':19, 'ctps':1234, 'contratação':2020, 'salário':1000}
#   (nome) tem valor (Jhonata)
#   (idade) tem o valor (19)
#   (ctps) tem o valor (1234)
#   (contratação) tem o valor (1000.00)
#   (aposentadoria) tem o valor (52)
#
#


