from dado import *
from persona import *
from arquivo import *

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
    escolhe = escolha('Digite: ')
    print(escolhe)
            
    #if escolha == 1:
    #elif escolha == 2:
    #elif escolha == 3:
    #    break



