# Desafio 080 - Crie um programa onde o usuário possa 
# digitar cinco valores numéricos e cadastre-os em uma 
# lista, já na posição (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

v_maior = 0
l_Valor = []
cont = 0
while cont < 5:
    
    v = int(input(f'Digite o {cont+1}° valor: '))

    for c in l_Valor:
        if cont == 0:
            l_Valor[0] = v
        elif v >= l_Valor[c]:
            l_Valor.insert(0, v)
        elif v <= l_Valor[c]:
            l_Valor.insert(-1, v)

    cont+=1
print(l_Valor)
