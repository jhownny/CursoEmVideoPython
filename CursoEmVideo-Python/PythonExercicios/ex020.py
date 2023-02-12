# Desafio 023 - Faça um programa que
# leia um número de 0 a 9999 e mostre
# na tela cada um dos digitos separados.

num = int(input('digite um numero de 0 a 9999\n: '))
# num: pode ter um numero de 0 a 9999
# num2: coloca espaço entre os numeros
# num3: substitui os espaços por ";"
# num3.split(";"): substitui as ";" por espaçamento separando os numeros por unidade

if num <= 9:
    print(f'O numero {num} é uma Unidade. ')

elif num >= 10 and num <= 99:

    num2 = " ".join(str(num))
    num3 = ';'.join(num2.split())
    dnum, unum = num3.split(";")
    print(f'Separando esses numeros'
          f'com as devidas identificações fica:'
          f' \nO numero {dnum} é um Dezena \nO '
          f'Numero {unum} é uma Unidade')

elif num >= 100 and num <= 999:

      num2 = " ".join(str(num))
      num3 = ';'.join(num2.split())
      cnum, dnum, unum = num3.split(";")
      print(f'Separando esses numeros com as devidas identificações fica:\n'
            f'O Numero {cnum} é uma Centena\n'
            f'O Numero {dnum} é uma Dezena\n'
            f'O Numero {unum} é uma Unidade')

elif num >= 1000 and num <= 9999:

      num2 = " ".join(str(num))
      num3 = ';'.join(num2.split())
      mnum, cnum, dnum, unum = num3.split(";")
      print(f'Separando esses numeros com as devidas identificações fica:\n'
            f'O Numero {mnum} é uma Milha\n'
            f'O Numero {cnum} é uma Centena\n'
            f'O Numero {dnum} é uma Dezena\n'
            f'O Numero {unum} é uma Unidade')

