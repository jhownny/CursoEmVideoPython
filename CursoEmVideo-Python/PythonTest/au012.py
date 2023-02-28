# Curso Python #012 - Condições Aninhadas

n = str(input('Qual é seu nome?'))
nome = n.upper()

if nome == 'JHONATA':
    print('que nome bonito!')

elif nome == 'PEDRO' or nome == 'JOÃO' or nome == 'MARIA':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'ANA CLÁUDIA JÉSSICA JULIANA':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')

print(f'tenha um bom dia, {nome}!')