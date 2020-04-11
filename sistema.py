from Trabalho.lib.interfaces import *
from Trabalho.lib.arquivo import *
from time import sleep

arq = 'Eleição.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar todos os Candidatos Cadastrados', 'Cadastrar Novo Candidato', 'Listar Votos por Candidato',
                     'Votos por região', 'Total de votos por Candidato', 'Desenvolvido por', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de Listar o conteúdo de um arquivo
        lerArquivo(arq)
        sleep(2)
    elif resposta == 2:
        # Opção para cadastrar um novo candidato
        cabeçalho('NOVO CADASTRO')
        cod_candidato = int(input('Código do Candidato: '))
        nome = str(input('Nome: ').strip().upper())
        cargo = str(input('Cargo do Candidato: ').strip().upper())
        regiao = str(input('Região: ').strip().upper())
        numVotos = int(input('Número de Votos: '))
        cadastrar(arq, cod_candidato, nome, cargo, regiao, numVotos)
        sleep(2)
        # Opção para mostrar os votos por candidato
    elif resposta == 3:
        cabeçalho2('Opção 3 - Mostrar os votos por candidato!')
        mostrarVotos(arq)
        sleep(1)
    # Opção para ver os totalizadores de votos por região
    elif resposta == 4:
        cabeçalho('Opção 4 - Lançar Votos por região')
        codCandidato = int(input('Código do Candidato: '))
        if codCandidato == cod_candidato:
            print('Código do Candidato ja cadastrado, vamos continuar!')
            nome = nome
            cargo = cargo
            regiao = str(input('Região:  '))
            numVotos = int(input('Número de votos: '))
            lancarVotos(arq, cod_candidato, nome, regiao, numVotos)
        else:
            print('Candidato ainda não cadastrado, continue com o cadastro!')
            nome = str(input('Nome do Candidato: '))
            cargo = str(input('Cargo: '))
            regiao = str(input('Região :'))
            numVotos = str(input('Número de Votos: '))
            cadastrar(arq, cod_candidato, nome, cargo, regiao, numVotos)
        sleep(1)
        # Opção para ver o total de votos por candidato
    elif resposta == 5:
        cabeçalho('Opção 5 - Total de Votos por Candidato')
        sleep(1)
        # Opção para ver quem desenvolveu o código
    elif resposta == 6:
        cabeçalho2('Opção 6 - Desenvolvido por')
        cabeçalho2('Jefferson Mike Chaves Ribeiro')
        sleep(1)
        # Opção para sair do Sistema
    elif resposta == 7:
        cabeçalho('Opção 7')
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        cabeçalho('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(2)
