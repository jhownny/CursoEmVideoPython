# Desafio 073 - Crie uma tupla preenchida com 20 
# primeiros colocados da tabela do campeonato 
# Brasileiro de Futebol, na ordem da colocação. 
# Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela. 
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

cont = 0
tupla = ('Botafogo','Grêmio', 'Flamengo', 'Palmeiras', 'Red Bull Bragantino', 
         'Fluminense', 'São Paulo', 'Chapecoense', 'Atletico-PR', 'Atlético-MG', 
         'Fortaleza', 'Cruzeiro', 'Cuiabá-MT', 'Santos', 'Bahia', 'Corinthians', 
         'Goiás', 'Vasco da Gama', 'América-MG', 'Coritiba' )

print('Os primeiros 5 colocados no campeonato Brasileiro de Futebol são:\n')

while cont <= 4:
    print(f'{tupla[cont]}, em {cont+1}° lugar na colocação.')
    cont+=1
    
print('=~' * 15)

cont = -1
print('Os últimos 4 colocados da tabela são: \n')

while cont != (-5):
    print(f'{tupla[cont]};')
    cont-=1

print('=~' * 15)

print(f'Times em ordem alfabética são: \n{sorted(tupla)}')


print('=~' * 15)

cont = 0
while True:
    if tupla[cont] == 'Chapecoense':
        print(f'O time {tupla[cont]} está em {cont+1}° lugar.')
        break
    
    cont+=1