# Curso Python #11 - Cores no Terminal

# Style ---------- Text ------------ BackGround
# 0 = None        | 30 = branco     | 40 = branco
# 1 = Bold        | 31 = vermelho   | 41 = vermelho
# 4 = Underline   | 32 = verde      | 42 = verde
# 7 = Negative    | 33 = amarelo    | 43 = amarelo
#                 | 34 = azul       | 44 = azul
#                 | 35 = roxo       | 45 = roxo
#                 | 36 = ciano      | 46 = ciano
#                 | 37 = cinza      | 47 = cinza

print('\033[4;37;40mopa,bão?\033[m')

a = 2
b = 3
nome = 'jhonata'

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print(f'Os valores são \033[32m {a} \033[m e \033[31m {b}')


print(f'Olá, muito prazer em te conhecer {cores["amarelo"]}{nome}{cores["limpa"]}!!!!')
