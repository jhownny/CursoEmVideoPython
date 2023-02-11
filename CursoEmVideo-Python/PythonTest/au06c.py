n = input('diga para min meu cumpadi \n :')

print('O tipo digitado é:{}'.format(type(n)))
print('{} é um numero? verdadeiro ou falso:{}'.format(n, n.isnumeric()))
print('{} é uma "string"? verdadeiro ou falso:{}'.format(n, n.isalpha()))
print('{} é um alfanumerico? verdadeiro ou falso:{}'.format(n, n.isalnum()))
print('{} é um ascii? verdadeiro ou falso:{}'.format(n, n.isascii()))
print('{} é uma letra em minuscula? verdadeiro ou falso:{}'.format(n, n.islower()))
print('{} é uma letra em maiuscula? verdadeiro ou falso:{}'.format(n, n.isupper()))
