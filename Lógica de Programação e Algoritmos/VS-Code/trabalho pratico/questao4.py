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
    print("[1] - Consultar Todos")
    print("[2] - Consultar por Id")
    print("[3] - Consultar por Setor")
    print("[4] - Retornar ao Menu")
    while True:
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            print(lista_colaboradores)
        elif opcao == 2:
            id = int(input("Digite o ID do colaborador: "))
            for c in lista_colaboradores:
                if(c['id'] == id):
                    print(c)
        elif opcao == 3:
            setor = input("Digite o Setor do colaborador: ")
            for c in lista_colaboradores:
                if c['setor'] == setor:
                    print(c)
        elif opcao == 4:
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
            print("Produto foi removido com sucesso.")
#Main
print("Bem vindo ao software de gerenciamento de pessoas de Emanuel Rosa Zolet!")
cadastrar_colaborador(id_global)
print(lista_colaboradores)
consultar_colaborador()
