# Desafio 110 - Adicione ao módulo moeda.py criado nos desafios 
# anteriores, uma função chamada resumo(), que mostre na tela 
# algumas informações geradas pelas funções que já temos no módulo 
# criado até aqui.

def resumo(num,taxa,redutaxa):
    print('-' * 30)
    print('     \033[1mRESUMO DO VALOR\033[m')
    print('-' * 30)
    print(f'Preço analizado:    R${num:.2f}')
    print(f'Dobro do Preço:     R${num*2:.2f}')
    print(f'Metade do preço:    R${num/2:.2f}')
    print(f'{taxa}% de aumento:     R${num+(num*taxa/100):.2f}')
    print(f'{redutaxa}% de redução:     R${num-(num*taxa/100):.2f}')
    print('-' * 30)


#Ex:

# from ex110 import moeda

#p = float(input('digite o preço: R$'))
# moeda.resumo(p,80,35)

#-----------------------
#   RESUMO DO VALOR
#-----------------------
#Preço analizado:   R$500,00
#Dobro do preço:    R$1000,00
#MEtade do preço:   R$250,00
#80% de aumento:    R$900,00
#35% de Redução:    R$325,00
#-----------------------
