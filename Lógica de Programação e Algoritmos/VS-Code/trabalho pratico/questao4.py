#variáveis globais
lista_colaboradores = []
id_global = 0
#Função para cadastrar colaborador, recebe o id como parametro e retorna o dicionario que será adicionado na lista de colaboradores.
def cadastrar_colaborador(id):
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite de que setor o colaborador pertence: ")
    pagamento = float(input("Digite o valor de pagamento do colaborador: R$ "))
    colaborador = {'id': id,'nome': nome, 'setor': setor, 'pagamento': pagamento}
    lista_colaboradores.append(colaborador)
#Função para consultar colaborador
def consultar_colaborador():
    while True:
        opcao = int(input("\nConsultando Colaborador:\n[1] - Consultar Todos\n[2] - Consultar por Id\n[3] - Consultar por Setor\n[4] - Retornar ao Menu\nDigite a opção desejada: "))
        if opcao == 1:
            for c in lista_colaboradores:
                print(f"\nID - {c['id']}\nNome - {c['nome']}\nSetor - {c['setor']}\nPagamento - R$ {c['pagamento']:.2f}")
        elif opcao == 2:
            id = int(input("Digite o ID do colaborador: "))
            for c in lista_colaboradores:
                if(c['id'] == id):
                    print(f"\nID - {c['id']}\nNome - {c['nome']}\nSetor - {c['setor']}\nPagamento - R$ {c['pagamento']:.2f}")
        elif opcao == 3:
            setor = input("Digite o Setor do colaborador: ")
            for c in lista_colaboradores:
                if c['setor'] == setor:
                    print(f"\nID - {c['id']}\nNome - {c['nome']}\nSetor - {c['setor']}\nPagamento - R$ {c['pagamento']:.2f}")
        elif opcao == 4:
            print("Retornando ao Menu!")
            return
        else:
            print("opção inválida!")  
            continue      
#Função para remover colaborador
def remover_colaborador():
    id = int(input("Digite o id do colaborador a ser removido: "))
    for c in lista_colaboradores:
        if c['id'] == id:
            lista_colaboradores.remove(c)
            print("Colaborador foi removido com sucesso.")
#Main
print("Bem vindo ao software de gerenciamento de pessoas de Emanuel Rosa Zolet!")
#Menu com opções
while True:
    menu = int(input("\nMENU\nDigite a opção desejada:\n[1] - Cadastrar Colaborador\n[2] - Consultar Colaborador\n[3] - Remover Colaborador\n[4] - Encerrar Programa\nSua Opção: "))
    if menu == 1:
        id_global += 1
        cadastrar_colaborador(id_global)
        continue
    elif menu == 2:
        consultar_colaborador()
        continue
    elif menu == 3:
        remover_colaborador()
        continue
    elif menu == 4:
        print("Encerrando Aplicação!")
        break
