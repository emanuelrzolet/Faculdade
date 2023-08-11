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
def salvar(colaborador,nomeArquivo):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Algo deu errado!')
    else:
        a.write(f'{colaborador};\n')
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
