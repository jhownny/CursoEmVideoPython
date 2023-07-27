
import moeda

v = float(input('Digite o preço: '))
p = int(input('Digite a porcentagem de aumento do valor: '))
print('=~' * 30)
print(f'O Dobro de {moeda.moeda(v)}: {moeda.moeda(moeda.dobro(v))}')
print(f'A Metade de {moeda.moeda(v)}: {moeda.moeda(moeda.metade(v))}')
print(f'O valor de {moeda.moeda(v)} com {p}% de Aumento: {moeda.moeda(moeda.aumentando(v,p))}')
print(f'O valor de {moeda.moeda(v)} com {p}% de Desconto: {moeda.moeda(moeda.diminuindo(v,p))}')
print('=~' * 30)