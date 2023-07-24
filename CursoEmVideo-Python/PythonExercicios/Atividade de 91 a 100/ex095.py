# Desafio 095 - Aprimore o DESAFIO 093 para que ele 
#funcione com vários jogadores, incluindo um sistema 
#de visualização de detalhes do aprovamento de cada 
#jogador.  

# (Desafio 093 - Crie um programa que gerencie o 
#   aproveitamento de um jogador de futebol. O programa 
#   vai ler o nome do jogador e qunatas partidasd ele jogou. 
#   Depois vai ler a quantidade de gols feitos em cada partida. 
#   No final, tudo isso será guardado em um dicionário, incluindo
#   o total de gols feitos durante o campeonato.)

jogadores=list()
jogador=dict()
lista=list()
while True:
    nome = str.title(input('Digite seu nome: '))
    jogador['nome'] = nome
    partidas = int(input('Digite a quantidade de partidas jogadas: ')) 
    jogador['partidas'] = partidas
    for i in range(partidas):
        gol = int(input(f'Digite quantos gols você fez na {i+1}° partida: '))
        lista.append(gol)
    total = sum(lista)
    jogador['gols'] = lista.copy()
    jogador['total'] = total
    jogadores.append(jogador.copy())
    lista.clear()
    continua = str.upper(input('Deseja continuar adicionando? [S/n]: '))
    if continua == 'N' or continua == 'NÃO':
        break
    
print(jogadores)
# Ultimo exercicio do capitulo 19


#
#
#
#
#
#
