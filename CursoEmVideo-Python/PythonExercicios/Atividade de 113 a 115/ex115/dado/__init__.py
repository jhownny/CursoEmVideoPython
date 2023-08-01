# Desafio 115 - Ccrie um pequeno sistema modularizado que permita 
# cadastratar pessoas pelo seu nome e idade em um arquivo de texto simple.

# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

def escolha(num):
    
    while True:
        try: 
            n = int(input(num))    
        except (ValueError, TypeError):
            print('Por Favor digite um valor valido presente acima')
            continue
        except KeyboardInterrupt:
            print(f'\033[1;31m\nVocê não digitou ou deixou em branco!\033[m')
            return 3
        else:
            try:
                if num 
  