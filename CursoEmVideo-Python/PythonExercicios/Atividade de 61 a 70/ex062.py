# Desafio 062 — Melhore o DESAFIO 061, perguntando
# para o utilizador se ele quer mostrar mais alguns
# termos. O programa encerra quando ele disser
# que quer mostrar O termo.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo_atual = primeiro_termo
contador = 1

while True:

    print(f'{termo_atual}', end=' -> ')
    termo_atual += razao
    contador += 1
    if contador == 10:
        print('Fim')
        pergunta = str.capitalize(input('\nDeseja adicionar mais termos?: '))
        if pergunta == "Sim" or pergunta == "S":
            contador = 1
            primeiro_termo = int(input('Digite o primeiro termo da PA: '))
            razao = int(input('Digite a razão da PA: '))
            termo_atual = primeiro_termo
        else:
            break