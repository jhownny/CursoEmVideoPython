# Desafio 014 - Escreva um programa
# que converta uma temperatura
# digitada em °c e converta para °F.

C = float(input('Informe a temperatura em °C:'))
F = (C*1.8) + 32

print('{}°C? Parece que a equivalencia a esse temperatura em Fahrenheit é: {:.1f}°F '.format(C, F))
