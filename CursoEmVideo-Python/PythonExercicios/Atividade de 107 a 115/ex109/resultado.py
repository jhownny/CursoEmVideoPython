
import moeda


v = float(input('Digite o preço: '))
p = int(input('Digite a porcentagem a ser calculada em cima do valor: '))
print('=~' * 30)
print(f'O Dobro de {moeda.moeda(v)}: {moeda.dobro(v,True)}')
print(f'A Metade de {moeda.moeda(v)}: {moeda.metade(v,True)}')
print(f'O valor de {moeda.moeda(v)} com {p}% de Aumento: {moeda.aumentando(v,p,True)}')
print(f'O valor de {moeda.moeda(v)} com {p}% de Desconto: {moeda.diminuindo(v,p,True)}')
print('=~' * 30)