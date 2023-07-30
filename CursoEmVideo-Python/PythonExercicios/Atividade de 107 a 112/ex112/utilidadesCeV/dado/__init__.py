
def LeiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print('\033[1;31mValor Digitado Incorreto ou Não Aceito.\nPorFavor Colocar Valor em Formato Numeral!\033[m ')
        else:
            valido = True
            return float(entrada)
    