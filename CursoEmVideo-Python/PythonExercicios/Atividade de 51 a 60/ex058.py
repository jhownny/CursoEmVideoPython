# Desafio 058 — Melhore o jogo do DESAFIO 028
# onde o computador vai "pensar" num número
# entre 0 e 10. Entretanto, agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

import random
num = random.randrange(0, 10)
user = int(input('Diga um número de 0 a 10: '))

if user == num:
    print(f'Olha só, você acertou! \nO numero que o computador sorteou foi o número: {num}')
else:
    while user != num:
        num = random.randrange(0, 10)
        int(input(f'parece que o número sorteado foi {num}, tente novamento: '))
print(f'Você CERTOU, o número que o computador sorteou foi o número: {num}')