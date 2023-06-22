# Curso Python #16 - Tuplas

#lanche = ('Hambúrguer', 'Suco', 'Pizza','Pudim')

#for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]}.')
#
#for pos, comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')
#    
#print('comi demais!!!')

#print(sorted(lanche))

#-------------------------------------------------------

#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = a + b
#print(c)

#--------------------------------------------------------

pessoa = ('Gustavo', 39, 'M', 99.88)

del(pessoa) # Permitido a exclusão da tupla inteira.
del(pessoa[0]) # Não permitida a exclusão de um elemento de dentro da tupla.

print(pessoa)