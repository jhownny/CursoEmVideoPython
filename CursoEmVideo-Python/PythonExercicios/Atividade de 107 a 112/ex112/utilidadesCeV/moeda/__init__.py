# Desafio 112 - Dentro do pacote utilidadesCeV que criamos no desafio 111, 
# temos um módulo chamado dado. crie um função chamada dinheiro() que seja 
# capaz de funcionar como função input(), mas com uma validação de dados 
# para aceitar apenas valores que sejam monetários.

def metade(num):
    num/=2
    return num


def dobro(num): 
    num*=2
    return num


def aumentando(num, taxa,):
    res = num + (num*taxa/100)
    return res


def diminuindo(num,taxa,):
    res = num - (num*taxa/100)
    return res


def moeda(num):
    return (f'R${num:.2f}')


def resumo(num,taxa,redutaxa):

    print('-' * 30)
    print('     \033[1mRESUMO DO VALOR\033[m')
    print('-' * 30)
    print(f'Preço analizado:    {moeda(num)}')
    print(f'Dobro do Preço:     {moeda(dobro(num))}')
    print(f'Metade do preço:    {moeda(metade(num))}')
    print(f'{taxa}% de aumento:     {moeda(aumentando(num,taxa))}')
    print(f'{redutaxa}% de redução:     {moeda(diminuindo(num,redutaxa))}')
    print('-' * 30)

#Ex:
# from ex112.utilidadesCeV import dado
#p = dado.leiaDinheiro('digite o preço: R$')
# moeda.resumo(p, 35, 22)