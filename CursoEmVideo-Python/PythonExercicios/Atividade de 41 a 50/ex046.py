# Desafio 049 - Refaça o DESAFIO 009, mostrando a
# tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

s = 0
n = int(input('Digite um valor para tabuada: '))
for t in range(10):
    s += 1
    v = n * s
    print(f'{n} x {s} = {v}')


