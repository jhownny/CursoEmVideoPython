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

  