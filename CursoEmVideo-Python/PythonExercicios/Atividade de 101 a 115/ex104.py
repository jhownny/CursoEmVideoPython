# Desafio 104 - Crie um rpograma que tenha a função 
# input() do Python, só que fazendo a validação para 
# aceitar apenas um valor numérico.
a = 0
def LeiaInt(a):
    
    if not a.isnumeric():
        while True:           
            print('\033[1;31mErro, Digite um numero\033[m')
            a = input('Digite um numero:')
            if a.isnumeric():
                break
        
    

LeiaInt(8)
print(f'você acabou de digitar o número {a}')

#EX: n = leiaInt('Digite um n')

#n = leiaint('Digite um número')
#print(f'Você acabou de digitar o número {n}')