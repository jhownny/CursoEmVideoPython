
# Desafio 011 - Faça um programa
# que leia a largura e a altura de
# uma parede em metros, calcule a
# sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que
# cada litro de tinta, pinta uma área de 2m²

L = float(input('Me diga a largura de sua parede em METROS: '))
A = float(input('Me diga a altura de sua parede em METROS: '))

Ar = (A * 2) + (L * 2)

print(f"Sabendo que você tem \n{L} metros de Largura e \n{A} metros de Altura, é necessario comprar"
      f" \n{Ar} Litros de tinta para pintar toda a parede.")
