from dado import *
from persona import *
from arquivo import *
from time import sleep

arq = "CursoEmVideo-Python/PythonExercicios/Atividade de 113 a 115/ex115/Cadastros.txt"

if not ArqExiste(arq):
    CriarArq(arq)

while True:

    linhazinha()
    LetraCor('      MENU PRINCIPAL',3,1)
    linhazinha()

    print('\033[;33m1 -\033[m \033[;34mVer Pessoas Cadastradas\033[m')
    print('\033[;33m2 -\033[m \033[;34mCadastrar nova Pessoa\033[m')
    print('\033[;33m3 -\033[m \033[;34mSair do Sistema\033[m')

    linhazinha()
    ecla = escolha('\033[1;35mDigite a operação desejada:\033[m ')

    if ecla == 1:
        LerArq(arq)
    elif ecla == 2:
        linhazinha()
        LetraCor('      NOVO CADASTRO',3,1)
        linhazinha()
        nome = str(input('\nNome: '))
        idade = LeiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif ecla == 3:
        LetraCor('\nAté breve...\n',7,1)
        break
    sleep(2)

