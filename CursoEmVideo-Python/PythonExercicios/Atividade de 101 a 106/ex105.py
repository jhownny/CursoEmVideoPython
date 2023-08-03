# Desafio 105 - Faça um programa que tenha um função notas() 
# que pode receber várias notas de alunos e vai retornar um 
# dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da Turma
# - A situação (Opcional)

# Obs: Adicione também as docstrings da função.

cont = 1
l=list()
d=dict()

def notas():

    """
    RECEBEDOR DE NOTAS

    Parâmetros:
    - n: O número inteiro cujo valor será processado para gerar diferentes resultados.

    Retorna:
    - O valor da maior nota;
    - O valor da menor nota;
    - A media de todas as notas inseridas;
    - A Quantidade de notas inseridas.
    """
    
    global maior_nota, menor_nota, media,cont
    while True:
        n = float(input(f'Digite a nota do {cont}° aluno: '))
        l.append(n) 
        d['Quant'] = cont
           
        l.sort()
        maior_nota = l[-1]
        menor_nota = l[0]
        soma = sum(l)
        media = (soma/cont)
        d['MaiorNota']= maior_nota
        d['MenorNota']= menor_nota
        d['Media']= media
        continuar = str.upper(input('Deseja continuar inserindo notas? [S/n]: '))
        if continuar == 'N' or continuar == 'NÃO':
            break
        cont+=1

notas()
print(f'\nTeve {cont} notas cadastradas, a lista de notas é {l}, a maior nota é {maior_nota}, a menor é {menor_nota} e a media de notas é {media:.2f}')
print(f'O dicionario resumido de todas essas informações é esse: {d}')
#resp = notas(5.5,9.5,6.5,sit=True)
#print(resp)
#help(notas)