# Desafio 093 - Crie um programa que gerencie o 
# aproveitamento de um jogador de futebol. O programa 
# vai ler o nome do jogador e qunatas partidasd ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo 
# o total de gols feitos durante o campeonato. 

jogador=dict()

nome = str.title(input('Digite seu nome: '))
partidas = int(input('Digite a quantidade de partidas jogadas: '))

cont= 0 
for j in range(partidas):
    if cont == 0:
        gol = int(input(f'quantos gols fez na {cont +1}° partida: '))
        jogador['gols'] = gol
    else:
        gol = int(input(f'quantos gols fez na {cont +1}° partida: '))
        jogador['gols'] = ([gol])    
    cont+=1
    
print(jogador)