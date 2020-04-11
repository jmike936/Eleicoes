from Trabalho.lib.interfaces import *
from time import sleep


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('CANDIDATOS CADASTRADOS')
        print('Cód:  Nome:                         Cargo:         Região:             Votos:')
        for linha in a:
            dado = linha.split(';')
            dado[0] = dado[0].replace('\n', '')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0].upper():<6}{dado[1].upper():30}{dado[2].upper():15}{dado[3].upper():20}{dado[4]:6>}')

    finally:
        a.close()


def cadastrar(arq, cod_candidato, nome='desconhecido', cargo='sem cargo', regiao='Sem região', numVotos='0'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{cod_candidato};{nome};{cargo};{regiao};{numVotos}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} cadastrado! ')
            a.close()


def mostrarVotos(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('VOTOS POR CANDIDATO')
        print('Cód:  Nome:                         Votos:')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0].upper():<6}{dado[1].upper():30}{dado[4]:6>}')

    finally:
        a.close()


def lancarVotos(arq, nome='Desconhecido', codCandidato='0', regiao='Sem Região', numVotos='0'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{codCandidato, nome, regiao, numVotos}')
        except:
            print('Houve um erro na hora de lançar os votos! ')
        else:
            print(f' Dados de {nome} Cadastrado com sucesso!')
            a.close()

