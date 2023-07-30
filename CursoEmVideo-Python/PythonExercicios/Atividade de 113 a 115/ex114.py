# Desafio 114 - Crie um código em Python que teste 
# se o site Pudim está acecssivel pelo computador usando.

from urllib import request

try:
    site = request.urlopen('http://www.pudim.com.br')
except:
    print('O site Pudim não está acessivel no momento')
else:
    print('O site pudim está no ar')
    