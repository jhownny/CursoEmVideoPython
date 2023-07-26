# Desafio 103 - Faça um programa que tenha uma função 
# chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou.

# O programa deverá ser capaz de mostrar a ficha 
# do jogador, mesmo que algum dado não tenha sido informado corretamente. 

def ficha(nome='<desconhecido>',gol=0):
    
    print(f"O jogador {nome} marcou {gol} gol(s).")

nome = input('Nome do jogador: ')
gol = input('Número de gols: ')

if nome.strip() == "":
    nome = "<desconhecido>"
if not gol.isdigit():
    gol = 0

    

ficha(nome, int(gol))
# Se nome do jogador e a quantidade de gols estiver vazia ira imprimir: 
#
# Nome do Jorgador: {vazio} 
# Número de Gols: {vazio}
# O jogador <desconhecido> fez 0 gol(s) no campionato.