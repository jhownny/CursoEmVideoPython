# Curso Python #09 - Manipulando Texto

frase = 'Curso em Video Python'

print('|C|u|r|s|o| |e|m| |V|i |d |e |o |  |P |y |t |h |o |n \n|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20\n ')

# |C|u|r|s|o| |e|m| |V|i |d |e |o |  |P |y |t |h |o |n
# |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20

# Exemplos com variaveis facilmente executaveis:

# Contando a quantidade de strings:
print(len(frase))

# apresenta somente as letras "o" MINUSCULAS do 0 ao 13:
print(frase.count('o,0,13'))

# indica a posição em que se encontra a frase solicitada:
print(frase.find('deo'))

# Existe a palavra Curso em frase?
print('curso'in frase)

# substitui strings apresentadas para strings solicitadas:
print(frase.replace('Python', 'Android'))

# Todas as letras maiusculas:
print(frase.upper())

# Todas as letras minusculas:
print(frase.lower())

# Só a primeira letra maiuscula:
print(frase.capitalize())

# vai transformar todas as primeiras letras depois do espaço em maiusculas:
print(frase.title())

# Divide as palavra em cadeia de caracteres:
print(frase.split())

# Adiciona "-" a cada espaço em entre as letras existente na frase:
print("-".join(frase))

# Adiciona "-" a cada espaço em branco existente na frase:
print('-'.join(frase.split()))

frase2 = '   Aprenda Python  '
print('\n| | | |A|p|r|e|n|d|a|  |P |y |t |h |o |n |  |  |\n|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|\n ')

# | | | |A|p|r|e|n|d|a|  |P |y |t |h |o |n |  |  |
# |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|

# (Right Strip) - Remove os espaços excedentes do lado Direito:
print(frase2.rstrip())

# (Left Strip) - Remove os espaços excedentes do lado Esquerdo:
print(frase2.lstrip())

# Remove os espaços excedentes entre os polos Esquerdo e Direito da frase:
print(frase2.strip())

