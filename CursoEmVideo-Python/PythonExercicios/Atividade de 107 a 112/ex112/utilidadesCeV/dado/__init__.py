
def LeiaDinheiro(msg):

    input(f'{msg}')

    while not msg.isnumeric():
        if msg.isnumeric():
            continue
        elif msg.isalpha():
            print('\033[1;31mValor Digitado Incorreto ou Não Aceito.\nPorFavor Colocar Valor em Formato Numeral!\033[m ')
        msg = input('Digite o Preço [Corretamente]: R$')

    