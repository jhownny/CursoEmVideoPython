# Desafio 044 - Elabore um programa que calcule o
# valor a ser pago por um produto, considerando o
# seu preço normal e condição de pagamento:
#
# á vista dinheiro/cheque: 10% de desconto;
# á vista no cartão: 5% de desconto;
# em até 2x no cartão: preço normal;
# 3x ou mais no cartão: 20% de juros.

valor = float(input('Qual o valor do valor do produto:'))
pagamento = int(input('\nQual seu metodo de pagamento?'
                      '\n1. Á Vista Dinheiro/Cheque'
                      '\n2. Á Vista no Cartão'
                      '\n3. Cartão de Crédito em até 2X(Sem Juros)'
                      '\n4. Cartão de Crédito em 3X ou Mais(Com Juros de 20%)'
                      '\n:'))

if pagamento == 1:
    print(f'\nO seu produto Á Vista ou em Cheque fica: R${valor - (valor * 0.10):.2f}')

elif pagamento == 2:
    print(f'\nO seu produto Á Vista no Cartão fica: R${valor - (valor * 0.5):.2f} ')

elif pagamento == 3:
    print(f'\nO seu produto em até 2X no cartão fica: R${valor / 2:.2f } por dois meses.')

elif pagamento == 4:
    parcelas = int(input(f'\nEm quanto pretende parcelar?\n:'))
    resultado = valor + (valor * 0.20)
    if parcelas <= 2:
        print(f'parcelas menores que 3x não pagam juros então você pagará: R${valor / 2:.2f} por 2 meses')
    else:
        print(f'Em {parcelas}x você pagará: R${resultado / parcelas:.2f} por mês. ')
