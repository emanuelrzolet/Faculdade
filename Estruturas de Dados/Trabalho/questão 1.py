# Inicialização da lista encadeada simples
class Cartao:
    # Exigência de código 1
    def __init__(self, cor):
        self.cor = cor
        self.numero = None
        self.proximo = None

class ListaCartoes:
    def __init__(self):
        self.head = None
        
    def inserirSemPrioridade(self, nodo):
        # Exigência de código 2
        if self.head is None:
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo is not None:
            nodo_atual = nodo_atual.proximo

        nodo_atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        # Exigência de código 3
        if self.head is None:
            self.head = nodo
            return

        anterior = None
        atual = self.head

        # Avança enquanto a cor for "A"
        while atual is not None and atual.cor == "A":
            anterior = atual
            atual = atual.proximo

        # Insere o nodo antes do primeiro "V" ou após os "A"
        if anterior is None:
            # Insere no início
            nodo.proximo = self.head
            self.head = nodo
        else:
            nodo.proximo = atual
            anterior.proximo = nodo


# Exemplo de uso:
lista = ListaCartoes()

def inserir():
    # Exigência de código 4
    cor = input("Digite a cor do cartão (A ou V): ").strip().upper()
    if cor not in ["A", "V"]:
        print("Cor inválida. Tente novamente.")
        return

    if not hasattr(inserir, "contador_v"):
        inserir.contador_v = 1
    if not hasattr(inserir, "contador_a"):
        inserir.contador_a = 201

    novo_cartao = Cartao(cor)
    if cor == "V":
        novo_cartao.numero = inserir.contador_v
        inserir.contador_v += 1
        lista.inserirSemPrioridade(novo_cartao)
    else:
        novo_cartao.numero = inserir.contador_a
        inserir.contador_a += 1
        lista.inserirComPrioridade(novo_cartao)
        
def imprimirListaEspera():
    # Exigência de código 5
    print("Lista de espera:")
    if lista.head is None:
        print("Lista de espera vazia.")
        return

    atual = lista.head
    while atual is not None:
        print(f"Cartão {atual.numero} - Cor: {atual.cor}")
        atual = atual.proximo
        
def atenderPaciente():
    # Exigência de código 6
    print("Atendendo paciente...")
    
    if lista.head is None:
        print("Nenhum paciente na lista de espera.")
        return

    atendido = lista.head
    lista.head = atendido.proximo
    print(f"Atendendo paciente com cartão {atendido.numero} - Cor: {atendido.cor}")
    del atendido  # Libera o nodo atendido da memória
    
    

# MAIN

while True:
    # Exigência de código 7
    print("\nMenu:")
    print("1 - Adicionar paciente à fila")
    print("2 - Mostrar pacientes na fila")
    print("3 - Atender paciente")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        inserir()
    elif opcao == "2":
        imprimirListaEspera()
    elif opcao == "3":
        atenderPaciente()
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")