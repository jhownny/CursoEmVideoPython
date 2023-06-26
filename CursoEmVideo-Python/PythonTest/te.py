print('Olá esse é um RPG interativo em teste!\n')
nome = str(input('Para começar digite o nome do seu personagem\n:'))
sexo = str.upper(input(f'\n{nome} é Mulher ou Homem?\n'))
while sexo != "MULHER" and "HOMEM":
      print(f'{sexo}? resultado diferente do solicitado')
print('\nAgora você precisa escolher uma categoria para seu personagem com as devidas qualidades:\n'
      'Ex-Fusileiro\n'
      'Medico\n'
      'Arquiteto\n'
      'alpinista\n')
status = str(input('Me diga que ponto de status você deseja upar no seu personagem:'))