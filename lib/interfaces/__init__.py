def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido. \033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar um número. \033[m')
            return 0
        else:
            return n


def linhas(tam=80):
    return '-' * tam


def cabeçalho(txt):
    print(linhas())
    print(txt.center(80))
    print(linhas())

def cabeçalho2(txt):
    print(txt.center(80))


def menu(lista):
    cabeçalho('\033[31mSISTEMA DE CONTROLE DE VOTOS DE UMA ELEIÇÃO\033[m')
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linhas())
    opc = leiaInt('\033[32mSua opção:\033[m ')
    return opc
