from persona import *

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True
    
    
def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ocorreu um ERRO ao criar o arquivo')
    else:
        print(f'Aquivo {nome} criado com sucesso!')
        

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        linhazinha()
        LetraCor('      PESSOAS CADASTRADAS',3,1)
        linhazinha()
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
    

def cadastrar(arq, nome='desconhecido', idade= 0):
    try:
        a = open(arq,'at')
    except:
        print('Ocorreu um erro na abertura do aquivo!')
    else:
        try:
            a.write(f'{nome};{idade}')
        except:
            print('Ocorreu um erro na escritura do arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()