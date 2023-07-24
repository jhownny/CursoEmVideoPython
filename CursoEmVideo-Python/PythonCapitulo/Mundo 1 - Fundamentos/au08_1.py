# Curso Python #08 - Utilizando Módulos

import math
nun = int(input('digite um numero: '))
raiz = math.sqrt(nun)
print(f'a raiz de {nun} é igual a {raiz:.2f}, aredondado para cima fica {math.ceil(raiz)} e para baixo fica {math.floor(raiz)}')