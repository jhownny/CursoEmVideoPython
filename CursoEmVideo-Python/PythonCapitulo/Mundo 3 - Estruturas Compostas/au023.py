# Curso Python #23 - Tratamento de Erros e Exceções

#try: # Operação.
#    a = int(input(f'Numerador: '))
#    b = int(input(f'Denominador: '))
#    r = a/b
#except: # Falhou.
#    print(f'Infelizmento tomou na jabiraca, o problema encontrado foi: ')
#else: # Deu Certo.
#    print(f'O resultado  é {r}')
#finally: # Vai ser executado independente do resultado.
#    print(f'Volte sempre! Muito obrigado')


#try: # Operação.
#    a = int(input(f'Numerador: '))
#    b = int(input(f'Denominador: '))
#    r = a/b
#except Exception as erro: # Falhou, Com tratamento.
#    print(f'Infelizmento tomou na jabiraca, o problema encontrado foi: {erro.__class__}')
#else: # Deu Certo.
#    print(f'O resultado  é {r}')
#finally: # Vai ser executado independente do resultado.
#    print(f'Volte sempre! Muito obrigado')


try: # Operação.
    a = int(input(f'Numerador: '))
    b = int(input(f'Denominador: '))
    r = a/b
except(ValueError, TypeError): # Falhou com os motivos especificados na chamada(valor e tipo de variavel digitados incorretamente).
    print('\nTivemos um problema com o tipo de dados que você digitou!')
except ZeroDivisionError:  # Falhou com os motivos especificados na chamada(valor não posse ser dividido por zero).
    print('\nNão é possivel dividir um número por zero!')
except KeyboardInterrupt:  # Falhou com os motivos especificados na chamada(valor não digitado prlo usuario [em branco]).
    print('\nO usuario PREFERIU não informar as dados!')
else: # Deu Certo.
    print(f'O resultado  é {r}.')
finally: # Vai ser executado independente do resultado.
    print(f'Volte sempre! Muito obrigado.')