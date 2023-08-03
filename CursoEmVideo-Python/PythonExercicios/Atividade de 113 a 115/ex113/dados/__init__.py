# Desafio 113 - Reescreva a função leiaInt() que fizemos no desafio 104, 
# incluindo agora a possibilidade da digitação de um numero de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def LeiaInt(msg):
    
    """
    LeiaInt -> Requere ao usuario a colocação de qualquer valor, mas só será aceito o valor que for numerico do tipo Int.

    Parâmetros:
        - Colocação de qualquer elemento, mas apenas será permitido aquele que for numerico do tipo Int.

    Retorna:
        - Retornara o valor que for numerico do tipo Int;
        - mensagem de erro exigindo correção.
        
    """

    while True:
        try: 
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31m ERRO, o Valor Digitado não se enquadra ao valor Requirido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[1;31m\nVocê não digitou ou deixou em branco!\033[m')
            return 0
        else:
            return n
        

def LeiaFloat(msg):

    """
    LeiaFloat -> Requere ao usuario a colocação de qualquer valor, mas só será aceito o valor que for numerico do tipo Float.

    Parâmetros:
        - Colocação de qualquer elemento, mas apenas será permitido aquele que for numerico do tipo Float.

    Retorna:
        - Retornara o valor que for numerico do tipo Float;
        - mensagem de erro exigindo correção.
        
    """

    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print(f'\033[1;31m ERRO, o Valor Digitado não se enquadra ao valor Requirido!\033[m')
            continue
        except:
            print(f'\033[1;31m\nVocê não digitou ou deixou em branco!\033[m')
            return 0
        else:
            return n 

