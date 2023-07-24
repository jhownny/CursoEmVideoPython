# Curso Python #15 - Interrompendo repetições while


cont = 1
while cont <= 10:
    print(cont, '->', end=' ')
    cont+=1
print('Acabou') 

#_______________________________________

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s+=n

print(f'a Soma dos numeros digitados deram {s}!')