# Curso Python #20 - Funções (Parte 1)

#def mostraLinha():
#    print('-=' * 25)
#
#
#mostraLinha()
#print('você que pensa bebezão!')
#mostraLinha()

######################################

#def título(txt):
#    print('-=' * 20)
#    print(txt)
#    print('-=' * 20)
#
#
#título('  SISTEMA DE ALUNOS   ')
#título('  Olá   ')
#título('  Bom Dia   ')

#########################################

#def soma(n,n2):
#    print(n + n2)
#
#
#soma(4,5)
#soma(8,9)
#soma(2,1)

###########################################

#def soma(n,n2):
#    print(f'A = {n} e B = {n2}')
#    print(f'A soma A + B = {n+n2}')
#
#
#soma(4,5)

############################################

#def contador(*num):
#    print(num)
#
#contador(2,1,7)
#contador(8,0)
#contador(4,4,7,6,2)   

##################################

#def contador(*num):
#    for valor in num:
#        print(f'{valor}',end='')
#
#contador(2,1,7)
#contador(8,0)
#contador(4,4,7,6,2)  

#####################################

#def contador(*num):
#    tam = len(num)
#    print(f'Recebi os valores {num} e são ao todo {tam} números.')
#
#
#contador(2,1,7)
#contador(8,0)
#contador(4,4,7,6,2)  

#######################################

#valores = [6, 3, 4, 7, 2, 0]
#def dobra(list):
#    pos = 0
#    while pos < len(list):
#        list[pos]*=2
#        pos+=1
#
#
#dobra(valores)
#print(valores)

########################################

def soma(*valores):
    s = 0
    for num in valores:
        s+=num
    print(f'somando os valores {valores} temos {s}')


soma(5,2)
soma(2,9,4)