# Curso Python #013 - Estrutura de repetição for
#
#for c in range(1, 6):
#    print('Oi')
#print('fim')
#-------------------------------------
#for c in range(1, 7, 2):
#    print(c)
#print('FIM')
#--------------------------------------
#n = int(input('digite um numero: '))
#for c in range(0, n+1):
#    print(c)
#print('fim')
#---------------------------------------------------
#i = int(input('Inicio: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))
#for c in range(i, f+1, p):
#    print(c)
#print('fim')
# -------------------------------------------------
s=0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')