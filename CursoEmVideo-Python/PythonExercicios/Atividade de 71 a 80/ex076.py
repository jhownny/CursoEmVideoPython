# Desafio 076 - Crie um programa que tenha 
# uma tupla única com nomes de produtos e seus 
# respectivos preço, na sequência.

# No final, mostre uma listagem de preços, 
# organizando os dados em forma tabular.

cont = 0
tupla = ('pão', 10.64, 'melancia', 11.50, 'cachorro', 100.75, 'chiclete', 1.25, 'açucar', 26.50)

for c in range(5):
    print(f'{tupla[cont]}|{tupla[cont+1]:.2f}')
    cont+=2