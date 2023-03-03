# Desafio 036 - Escreva um programa para
# aprovar o empréstimo bancário para a
# compra de uma casa. O programa vai
# perguntar o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar.
#
# Calcule o valor da prestação
# mensal, sabendo que ela não
# pode exceder 30% do salário ou
# então o empréstimo será negado.

casa = float(input('Diga-me o valor da\033[1;33m Residência\033[m: '))
salario = float(input('Diga-me sua\033[1;34m Renda Mensal\033[m: '))
tempo = int(input('Informe a sua\033[1;35m Estipulação Anual de Pagamento\033[m: '))

saporcento = (30 * salario) / 100
mensalidade = tempo * 12

if saporcento >= casa / mensalidade:
    print(f'Fizemos a cotação do sua\033[1;34m Renda Mensal,\033[m com o valor da\033[1;33m Residência\033[m '
          f'e junto com a\033[1;35m Estipulação Anual de Pagamento\033[m e o resultado é que'
          f'\n:Seu Emprestimo foi\033[1;32m Liberado\033[m!')
elif saporcento <= casa / mensalidade:
    print(f'Fizemos a cotação do sua\033[1;34m Renda Mensal,\033[m com o valor da\033[1;33m Residência\033[m '
          f'e junto com a\033[1;35m Estipulação Anual de Pagamsento\033[m e o resultado é que'
          f'\n:Seu Emprestimo foi\033[1;31m Recusado\033[m!')
else:
    print('\033[1;35m ERRO, dados informados não coincidem. ')
