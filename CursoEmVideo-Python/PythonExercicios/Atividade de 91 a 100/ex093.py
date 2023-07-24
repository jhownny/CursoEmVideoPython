# Desafio 093 - Crie um programa que gerencie o 
# aproveitamento de um jogador de futebol. O programa 
# vai ler o nome do jogador e qunatas partidasd ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo 
# o total de gols feitos durante o campeonato. 

jogador=dict()
lista=list()
nome = str.title(input('Digite seu nome: '))
partidas = int(input('Digite a quantidade de partidas jogadas: '))
jogador["nome"] = nome
for i in range(partidas):
    gol = int(input(f'Digite quantos gols você fez na {i+1}° partida: '))
    lista.append(gol)
jogador['gols'] = lista
total = sum(lista)
jogador['total'] = total
print('-=' * 20)
print(f'{jogador["nome"]} fez um total de {jogador["total"]} gols em {partidas} partidas!')
print('-=' * 20)
for c in range(partidas):
    print(f'{jogador["nome"]} na {c+1}° partida fez {lista[c]} gols!')

#base:
#
# {'nome': str ,'gols': [(int)] ,'total': (int) }
#
