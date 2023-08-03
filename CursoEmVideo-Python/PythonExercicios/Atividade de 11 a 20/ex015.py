# Desafio 015 - Escreva um programa que pergunte a
# quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.

# Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por Km rodado.

d = int(input('Quantos dias você ficou com o veículo?'))
k = float(input('Quantos Km foram rodados com o veículo?'))

pd = d * 60
pk = k * 0.15


print(f'Como você percorreu {k:.2f} Km e ficou com o veículo {d} dias você terá que pagar um total de R${pd + pk:.2f}')
