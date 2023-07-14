# Desafio 089 - Crie um programa que leia nome e duas 
# notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e 
# permita que o usuário possa mostrar as notas de cada aluno 
# individualmente

cont = 0 
l = [[],[],[]]

# Loop principal, Resposavel por armazenar os nomes e as notas dentro da lista.
while True:
    # adiciona a função "Contador" à lista.
    l[0].append(cont)

    # Usuario coloca o nome do aluno, logo em seguida armazena a mesma dentro da lista.
    nome = str.title(input(f'Digite o nome do {cont+1}° aluno: '))
    l[1].append(nome)

    # Usuario coloca a primeira e segunda nota, logo em seguida armazena as mesmas dentro da lista em sequência.
    nota1 = float(input(f'Digite a 1° nota do aluno {nome}: '))
    nota2 = float(input(f'Digite a 2° nota do aluno {nome}: '))
    l[2].append(nota1)
    l[2].append(nota2)
    cont+=1

    # Responsavel por parar o loop caso o usuario digite "n" ou "não"
    pergunta = str.upper(input('Deseja Adicionar mais um Aluno? [S/n]: '))
    if pergunta == 'N' or pergunta == 'NÃO':
        break


print('\nNo.   Nome   Média')
print('-'*20)
cont_arevolta = 0
cont_media = 0

# Segundo loop, Responsavel por mostrar a tabela com os alunos e suas devidas notas e posições. 
while cont > (0): 

    print(f'{l[0][cont_arevolta]} \xA0 \xA0 {l[1][cont_arevolta]} \xA0 {((l[2][cont_media] + l[2][cont_media+1])/2):.1f}')

    # cont_media = 0..2..4..6..8
    cont_media+=2

    #cot_arevolta = 0..1..2..3..4
    cont_arevolta+=1

    # cont = 4..3..2..1..0
    cont-=1
    
# Terceiro loop, Responsavel por mostrar a primeira e segunda nota de um aluno, escolhida pelo usuario.
while True:
    mnota = int(input('Mostrar nota de qual aluno? (999 interrompe): '))

    # loop que percorrerá toda a lista de indice 0 a procura do valor digitado pelo usuario na varivél "mnota".
    for no in l[0]:
        if mnota == l[0][no]:
                print(f'O  Aluno "{l[1][no]}" Tirou {l[2][no+mnota]} na primeira prova e {l[2][no+(mnota+1)]} na segunda ')

    # O loop encerrará caso o usuario digite "999".
    if mnota == 999:
        break

# Ultimo exercicio do capitulo 18 (17_2.0)