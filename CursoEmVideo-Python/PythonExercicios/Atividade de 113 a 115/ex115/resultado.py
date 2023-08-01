from dado import *
from persona import *
from arquivo import *
from time import sleep

arq = "CursoEmVideo-Python\PythonExercicios\Atividade de 113 a 115\ex115\oarquivo.txt"

if not arquivoexiste(arq):
    criararquivo(arq)

while True:

    linhazinha()
    LetraCor('      MENU PRINCIPAL',3,0)
    linhazinha()

    print('\033[;33m1 -\033[m \033[;34mVer Pessoas Cadastradas\033[m')
    print('\033[;33m2 -\033[m \033[;34mCadastrar nova Pessoa\033[m')
    print('\033[;33m3 -\033[m \033[;34mSair do Sistema\033[m')

    linhazinha()
    es = escolha(LetraCor('Digite: ',10,9))

    if es == 1:
        print('Lista')
    elif es == 2:
        print('nova pessoa')
    elif es == 3:
        break
    sleep(2)
            
    #if escolha == 1:
    #elif escolha == 2:
    #elif escolha == 3:
    #    break



