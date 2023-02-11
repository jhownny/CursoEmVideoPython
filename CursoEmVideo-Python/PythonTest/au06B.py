n = input('digite algo \n :')

if n.isalpha():
    print('{} é uma letra meu bom rapas.'.format(n))
elif n.isnumeric():
    print('{} é de fato um numero.'.format(n))
elif n.isalnum() :
    print('Porque {}? Tá maluco? ):<'.format(n))
else:
    print('Se que sabe então.')
