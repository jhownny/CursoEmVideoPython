# Desafio 101 - Crie um programa que tenha uma função 
# chamada voto() que vai receber como parâmetro o ano de 
# nascimento de uma pessoa, retornando uma valorliteral 
# indicando se uma pessoa tem voto NEGADO, OPCIONAL ou 
# OBRIGATÓRIO nas eleições.
from datetime import datetime

def voto(ano):

    """
    -> Diz se tem que votar ou não de acordo com a Idade
    :ano: Ano de nascimento do usúario
    """

    Hoje = datetime.now()
    idade = Hoje.year - ano
    if idade < 18:
        print(f'Você tem {idade} anos')
        print('VOTO NEGADO!')
    elif idade < 65:
        print(f'Você tem {idade} anos')
        print('VOTO OBRIGATÓRIO!')
    elif idade >= 65:
        print(f'Você tem {idade} anos')
        print('VOTO OPCIONAL!')   

voto(int(input('Digite qual é seu ano de nascimento: ')))