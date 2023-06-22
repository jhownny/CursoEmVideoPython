# Desafio 073 - Crie uma tupla preenchida com 20 
# primeiros colocados da tabela do campeonato 
# Brasileiro de Futebol, na ordem da colocação. 
# Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela. 
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

cont = 0
tupla = ('São Paulo','Palmeiras', 'Corinthians', 'São Bernado', 'Chapecoense', 'Fluminense', 'Tocantins', 'Minas Gerais', 'Bahia', 'Hsdgsfg',     'Ghdhdg', 'Ghdghdf', 'Fghdfgh', 'Gdhgfhfd', 'Reyjejj', 'Jhfdhjfghj', 'Alabama', 'Dghdhgdh', 'Beybety', 'Gdfhghd' )
tuplaAlpha = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',)
print(f'Os primeiros 5 colocados no campeonato Brasileiro de Futebol são:')

while cont <= 4:
        print(f'{tupla[cont]}, em {cont+1}° lugar na colocação.')
        cont+=1
    
print('======================================================================')

cont = -1
print('Os últimos 4 colocados da tabela são: ')

while cont != (-5):
    print(f'{tupla[cont]}, em uma das ultimas colocações.')
    cont-=1

print('======================================================================')
#cont = -1
#contAlpha = 0
#while True:
#    a = tupla[cont].count(tuplaAlpha[contAlpha], 0)
#    if a == 1:
#        print(f'{tupla[cont]}')
#        contAlpha+=1
#        cont = -1
#    cont-=1

print('======================================================================')
cont = 0
while True:
    if tupla[cont] == 'Chapecoense':
        print(f'O time {tupla[cont]} está em {cont+1}° lugar.')
        break
    cont+=1