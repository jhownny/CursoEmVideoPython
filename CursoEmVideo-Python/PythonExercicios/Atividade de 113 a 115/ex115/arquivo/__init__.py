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
        print('aa')
    else:
        print('bb')
        
def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro')
    else:
        print('aaa')
    
    