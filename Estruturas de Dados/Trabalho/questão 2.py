class ElementoDaListaSimples: 
    def __init__(self, chave=None, dado=None):
        # EXIGÊNCIA DE CÓDIGO 2 de 7:
        # Implementação do nodo que representa um estado com sigla, nomeEstado e ponteiro para o próximo
        self.chave = chave
        self.dado = dado
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self):
        # EXIGÊNCIA DE CÓDIGO 2 de 7:
        # Cada posição da tabela hash representa a cabeça (head) da lista encadeada
        self.head = None

    def inserir(self, chave, dado):
        # EXIGÊNCIA DE CÓDIGO 3 de 7:
        # Inserção sempre no início da lista encadeada
        nodo = ElementoDaListaSimples(chave, dado)
        nodo.proximo = self.head
        self.head = nodo 

    def remover(self, chave):
        atual = self.head
        anterior = None
        while atual:
            if atual.chave.upper() == chave.upper():
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.head = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def imprimir(self):
        # EXIGÊNCIA DE CÓDIGO 4 de 7:
        # Impressão das siglas de todos os nodos na lista encadeada de uma posição
        atual = self.head
        while atual:
            print(f"[{atual.chave}] ->", end=" ")
            atual = atual.proximo
        print("None")

class TabelaHash:
    def __init__(self):
        # EXIGÊNCIA DE CÓDIGO 1 de 7:
        # Tabela hash com 10 posições, inicialmente todas com None (por meio das listas encadeadas)
        self.tam = 10
        self.h = [ListaEncadeadaSimples() for _ in range(self.tam)]

    def hashFunc(self, k):
        # EXIGÊNCIA DE CÓDIGO 5 de 7:
        k = k.upper()
        if k == "DF":
            return 7
        return (ord(k[0]) + ord(k[1])) % self.tam

    def inserir(self, chave, dado):
        pos = self.hashFunc(chave)
        self.h[pos].inserir(chave, dado)

    def remover(self, chave):
        pos = self.hashFunc(chave)
        return self.h[pos].remover(chave)

    def imprimir(self):
        # EXIGÊNCIA DE CÓDIGO 4 de 7 (continuação):
        # Impressão das listas separadas por posição da tabela hash
        for i in range(self.tam):
            print(f"Posição {i}:", end=" ")
            self.h[i].imprimir()

def inserir_estados(tabela):
    # EXIGÊNCIA DE CÓDIGO 6 de 7:
    # Inserção dos 27 estados + DF na tabela hash
    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
        ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
        ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
        ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
        ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
    ]
    for sigla, nome in estados:
        tabela.inserir(sigla, nome)

def inserir_estado_ficticio(tabela):
    # EXIGÊNCIA DE CÓDIGO 7 de 7:
    # Inserção de um estado fictício com sigla formada pela primeira letra do nome + última do sobrenome
    tabela.inserir("EZ", "Emanuel Zolet")

# Programa principal
if __name__ == "__main__":
    tabela = TabelaHash()
    print()
    print("\n== Exigência de saída de console 1: Tabela hash inicial ==")
    tabela.imprimir()

    inserir_estados(tabela)
    print("\n== Exigência de saída de console 2: Tabela hash após inserir os 27 estados ==")
    tabela.imprimir()

    inserir_estado_ficticio(tabela)
    print("\n== Exigência de saída de console 3: Tabela hash após inserir os 27 estados + estado fictício ==")
    tabela.imprimir()

    while True:
        print('\n--- MENU ---')
        print('1 - Inserir na tabela hash')
        print('2 - Remover na tabela hash')
        print('3 - Listar a tabela hash')
        print('4 - Sair')

        op = input("Escolha uma opção: ")

        if op == "1":
            chave = input('Digite a sigla de um estado: ').upper()
            dado = input('Digite o nome do estado: ')
            tabela.inserir(chave, dado)
        elif op == "2":
            chave = input('Digite a sigla do estado que deseja remover: ')
            if tabela.remover(chave):
                print(f"{chave} removido com sucesso.")
            else:
                print(f"{chave} não encontrado.")
        elif op == "3":
            tabela.imprimir()
        elif op == "4":
            print('Encerrando...')
            break
        else:
            print("Opção inválida! Tente novamente.")
