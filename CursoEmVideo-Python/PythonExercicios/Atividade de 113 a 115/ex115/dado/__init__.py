# Desafio 115 - Ccrie um pequeno sistema modularizado que permita 
# cadastratar pessoas pelo seu nome e idade em um arquivo de texto simple.

# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

def escolha(num):
    
    while True:
        try: 
            n = int(input(num))    
        except (ValueError, TypeError):
            print('\033[1;31mPor Favor digite um valor valido sugerido acima\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31m\nVocê não digitou ou deixou em branco!\033[m')
            return 3
        else:
            if n == 1 or n == 2 or n == 3:
                return n
            else:
                print('\033[1;31mPor Favor digite um valor valido sugerido acima\033[m')
                continue


def LeiaInt(msg):
    
    """
    LEIAINT -> Requere ao usuario a colocação de qualquer valor, mas só será aceito o valor que for numerico do tipo Int.

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