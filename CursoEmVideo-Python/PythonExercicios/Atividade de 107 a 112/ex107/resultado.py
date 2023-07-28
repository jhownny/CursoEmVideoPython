
import moeda

v = float(input('Digite o preço: '))
p = int(input('Digite a porcentagem de aumento do valor: '))
print('=~' * 30)
print(f'O Dobro de R${v:.2f}: R${moeda.dobro(v):.2f}')
print(f'A Metade de R${v:.2f}: R${moeda.metade(v):.2f}')
print(f'O valor de R${v:.2f} com {p}% de Aumento: R${moeda.aumentando(v,p):.2f}')
print(f'O valor de R${v:.2f} com {p}% de Desconto: R${moeda.diminuindo(v,p):.2f}')
print('=~' * 30)