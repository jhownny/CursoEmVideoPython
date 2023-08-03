# Desafio 042 - Refaça o DESAFIO 035 dos
# triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:
#
# Equilátero: todos os lados iguais;
# Isósceles: dois lados iguais;
# Escalenos: todos os lados diferentes.

reta1 = int(input('Me informe as três medidas das retas\n:'))
reta2 = int(input(':'))
reta3 = int(input(':'))

# Caso dê certo apresenta o resultado.
if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    print('\nFecha um triângulo em meu querido!')

    # Caso todos os lados sejam iguais, apresenta a mensagem.
    if reta1 == reta2 and reta2 == reta3 and reta3 == reta1:
        print('É um \033[1;35mTriângulo Equilatero\033[m!')

    # Caso somente dois lados digitados sejam iguais, apresenta a mensagem.
    elif reta1 == reta2 != reta3 or reta3 == reta2 != reta1 or reta1 == reta3 != reta2:
        print('É um \033[1;34mTriângulo Isósceles\033[m!')

    # Caso todos os lados digitados sejam diferentes apresenta, a mensagem.
    elif reta1 != reta2 != reta3 != reta2 != reta3 != reta1:
        print('É um \033[1;33mTriângulo Escaleno\033[m!')

# Caso não de certo apresenta a mensagem
else:
    print('\033[1;31mFechou não, meu bom.\033[m')
