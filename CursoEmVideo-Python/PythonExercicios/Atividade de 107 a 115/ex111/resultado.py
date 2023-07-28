

from utilidadesCeV import moedas,dados

v = float(input('Digite o preço: '))
p = int(input('Digite a porcentagem a ser calculada em cima do valor: '))
print('=~' * 30)
print(f'A Metade de R${(v)}: {moedas.metade(v,True)}')