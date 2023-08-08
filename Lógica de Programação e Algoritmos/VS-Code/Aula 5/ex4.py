def destaque(palavra):
    print("+" + "-"* (len(palavra)) + "+")
    print("|" + palavra + "|")
    print("+" + "-"* (len(palavra)) + "+")
def validar():
    r = input("Digite a opção desejada: ")
    while r not in "1,2,sair":
        print("valor digitado é incorreto.")
        r = input("Digite a opção desejada: ")
    return r
def cadastrar(nome,plataforma,nomeArquivo):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Algo deu errado!')
    else:
        a.write(f'{nome};{plataforma}\n')
    finally:
        a.close()
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())
    finally:
        a.close()
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: return True
def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nomeArquivo} foi criado com sucesso!\n')

#Programa Principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print(destaque("MENU DE OPÇÔES\n[1] - Cadastrar novo item\n[2] - Listar itens\n[sair] - Encerrar aplicação"))
    r = validar()
    if r == "sair":
        print("Encerrando Programa!")
        break
    elif r == "1":
        print("Opção de Cadastrar novo item selecionada...\n")
        nome = input("Digite o nome do jogo: ")
        plataforma = input("Digite qual plataforma o jogo pertence: ")
        cadastrar(nome,plataforma,arquivo)
    elif r == "2":
        print("Opção de listar itens selecionada...\n")
        listarArquivo(arquivo)
        continue