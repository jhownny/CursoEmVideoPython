# Desafio 057 - Faça um programa que
# leia o sexo de uma pessoa, mas só
# aceite os valores 'M' ou 'F'.
#
# Caso esteja errado peça a digitação
# novamente até ter um valor correto.

sexo = 'p'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu Sexo com M (Masculino) e F (Feminino): ')).upper()
if sexo == 'M':
    print(f'Ok, seu sexo é {sexo}asculino.')
else:
    print(f'Ok, seu sexo é {sexo}eminino.')