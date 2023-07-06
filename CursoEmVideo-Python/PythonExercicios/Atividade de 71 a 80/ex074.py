# Desafio 077 - Crie um programa que tenha uma tupla com 
# várias palavras (não usaracentos). Depois disso, você 
# deve mostrar, para cada palavra, quais são suas vogais.

cont = 0
palavras = ('macaco', 'cachorro', 'lapis', 'borracha', 'monitor', 'calendario', 'janela', 'antetiguimon', 'uva')

while True:
    if cont == len(palavras):
        break
    listaVogais = []
    lista = list(palavras)
    separado = list(lista[cont])
    for c in separado:
        if c == 'a':
            listaVogais.append(c)
        if c == 'e':
            listaVogais.append(c)
        if c == 'i':
            listaVogais.append(c)
        if c == 'o':
            listaVogais.append(c)
        if c == 'u':
            listaVogais.append(c)
    print(f'A palavra "{palavras[cont].capitalize()}" tem as vogais {listaVogais};')
    if cont == len(palavras):
        break
    cont+=1

# Ultimo exercicio do capitulo 16