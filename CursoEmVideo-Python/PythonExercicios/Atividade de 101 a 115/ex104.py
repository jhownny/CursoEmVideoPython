# Desafio 104 - Crie um rpograma que tenha a função 
# input() do Python, só que fazendo a validação para 
# aceitar apenas um valor numérico.

def inputer():

    """
    INPUTER -> Requere ao usuario a colocação de qualquer valor, mas só será aceito o valor que for numerico.

    Parâmetros:
    - Colocação de qualquer elemento, mas apenas será permitido aquele que for numerico.

    Retorna:
    - Retornara o valor que for numerico;
    - mensagem de erro exigindo correção.
    """

    while True:
        valor = input('Digite um valor: ')
        if valor.isnumeric():
            print(f'\nVocê acabou de digitar o número: {valor}')
            break
        else:
            print(f'\033[1;31m ERRO, o Valor "{valor.upper()}" Digitado não se enquadra ao valor Requirido!\033[m')

inputer()


#EX: n = leiaInt('Digite um n')

#n = leiaint('Digite um número')
#print(f'Você acabou de digitar o número {n}')