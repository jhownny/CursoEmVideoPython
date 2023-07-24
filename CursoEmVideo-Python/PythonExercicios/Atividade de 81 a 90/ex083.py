# Desafio 083 - Crie um propgrama onde o usúario digite 
# uma expressão qualquer que use parênteses. Seu aplicativo 
# deverá analisar se a expressão passada está com os 
# parênteses abertos e feçados na ordem correta.
l = []
exp = str.upper(input('Digite a expresão: '))
for simb in exp:
    if simb =='(':
        l.append('(')
    elif simb ==')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está equivocada!')


#for c in exp:
    
# Exe: ((a+b) * c / (d-e))

# Ultimo exercicio do capitulo 17


