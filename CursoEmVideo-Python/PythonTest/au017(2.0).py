# Curso Python #17 - Listas (Parte 2)

#teste = []
#teste.append('jhonata')
#teste.append(19)
#galera = []
#galera.append(teste[:])
#teste[0] = 'paulo'
#teste[1] = 22
#galera.append(teste[:])
#print(galera)

#===============================

galera = [['jhonata', 19],['pedro', 5],['paula', 346],['jaimundolynson', 9]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])

#===============================

#galera = [['jhonata', 19],['pedro', 5],['paula', 346],['jaimundolynson', 9]]
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos de idade.')

#================================

#galera = []
#dado = []
#for c in range(0,3):
#    dado.append(str(input('Nome: ')))
#    dado.append(str(input('Idade: ')))
#    galera.append(dado[:]) #<--- O "[:]" é copia de uma lista para outra sem necessariamente modifica-lá (Copia limpa.)
#    dado.clear()
#
#print(f'{galera}')

#=================================

#galera = []
#dado = []
#totmai = totmen = 0
#for c in range(0,3):
#    dado.append(str(input('Nome: ')))
#    dado.append(str(input('Idade: ')))
#    galera.append(dado[:]) 
#    dado.clear()
#
#for p in galera:
#    if p[1] >= 21:
#        print(f'{p[0]} é maior de idade')
#        totmai += 1
#    else:
#        print(f'{p[0]} é menor de idade')
#        totmen += 1
#
#print(f'Temos {totmai}  maiores de idade e {totmen} menores de idade.')