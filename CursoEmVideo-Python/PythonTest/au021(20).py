# Curso Python #21 - Funções (Parte 2)

#def fatorial(num=1):
#    f =1
#    for c in range(num,0,-1):
#        f+=c
#    return f
#
#
#f1 = fatorial(5)
#f2 = fatorial(4)
#f3 = fatorial(1)
#print(f'Os resultados são {f1}, {f2} e {f3}')

###################################################

#def par(n=0):
#    if n%2 == 0:
#        return True
#    else:
#        return False
#    
#num = int(input('digiote um numero:'))
#if par(num):
#    print('é par')
#else:
#    print('não é par')

################# Help Function #################

#print(input.__doc__)
#help(input)

#def contador(i,f,p):
#    """
#    ->Faz uma contagem e mostra na tela.
#    :param i: início da contagem
#    :param f: fim da contagem
#    :param p: passo da contagem
#    :return: sem retorno
#    """
#    c=1
#    while c <=f:
#        print(f'{c}',end='  ')
#        c+=p
#    print('fim!')
#
#
#help(contador)
#contador(2,10,2)

#def somar(a=0,b=0,c=0):
#    s=a+b+c
#    print(f'A soma vale {s}')
#
#somar(3,2,5)
#somar(8,4)
#somar()

#def teste(b):
#    a=8
#    b+=4
#    c=2
#    print(f'"A" Dentro vale {a}')
#    print(f'"B" Dentro vale {b}')
#    print(f'"C" Dentro vale {c}')
#
#
#a=5
#teste(a)
#print(f'"A" Fora vale {a}')
#
#def teste(b):
#    global a
#    a=8
#    b+=4
#    c=2
#    print(f'"A" Dentro vale {a}')
#    print(f'"B" Dentro vale {b}')
#    print(f'"C" Dentro vale {c}')
#
#
#a=5
#teste(a)
#print(f'"A" Fora vale {a}')

def somar(a=0,b=0,c=0):
    s=a+b+c
    return s 


r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')