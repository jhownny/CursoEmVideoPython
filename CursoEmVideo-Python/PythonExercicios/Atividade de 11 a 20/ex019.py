# Desafio 019 - Um professor quer sortear um
# dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.

import random

nomes1 = 'João','Pedro','Geovana','Cladio'

aluno = random.choice(nomes1)

print(aluno)