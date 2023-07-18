# Desafio 090 - faça um programa que leia nome e média 
# de um aluno, guardando também a situação em um dicionári. 
# No final, mostre conteúdo da estrutura na tela. 

aluno = {'nome':0,'média':0}
nome = str.title(input('Digite o nome do aluno: '))
media = float(input('Digite a media do aluno: '))
aluno['nome'] = nome
aluno['média'] = media

print(f'O nome do aluno é {aluno["nome"]} e a média dele é {aluno["média"]}!')