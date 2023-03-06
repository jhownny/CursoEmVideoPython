# Curso Python #014 - Estrutura de repetição while

c=1
while c < 10:
   print(c)
   c = c + 1
print('fim')
#----------------------------------------
n =1
while n != 0:
    n = int(input('Digite um valor: '))
print('fim')
#----------------------------------------
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer Continuar? [S/N')).upper()
print('fim')
#----------------------------------------
n =1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar = 1
print(f'Você digitou {par} números pares e {impar} números impares!')