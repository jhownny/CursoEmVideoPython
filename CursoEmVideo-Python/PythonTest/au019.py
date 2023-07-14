# Curso Python #19 - Dicionários
#
#pessoas = {'nome':'jhonata','sexo':'M','idade':19}
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

#---------------------------------------------------

#pessoas = {'nome':'jhonata','sexo':'M','idade':19}
#for k, v in pessoas.items():
#    print(f'{k} = {v}')
#

#---------------------------------------------------

#pessoas = {'nome':'jhonata','sexo':'M','idade':19}
#pessoas['nome'] = 'leandro'
#
#for k, v in pessoas.items():
#    print(f'{k} = {v}')

#---------------------------------------------------

#brasil = []
#estado1 = {'uf':'São Paulo','sigla':'SP'}
#estado2 = {'uf':'Rio de Janeiro','sigla':'RJ'}
#brasil.append(estado1)
#brasil.append(estado2)
#
#print(brasil)
#print(brasil[0])
#print(brasil[1])
#print(brasil[0]['uf'])
#print(brasil[1]['sigla'])

#---------------------------------------------------

estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input(f'Unidade Federativa: '))
    estado['sigla'] = str(input(f'Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()