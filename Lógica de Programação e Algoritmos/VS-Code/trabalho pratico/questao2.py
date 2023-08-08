#Inicialização da variavel de valor total do pedido
valorTotal = 0
#Apresentação e Cardápio
print("Bem vindo a sorveteria de Emanuel Rosa Zolet!")
print("_-" * 20, 'Menu', '_-' * 22)
print('|  Nº de Bolas  |  Sabor Tradicional (tr)  |  Sabor Premium (pr)  |  Sabor Especial (es)  |')
print('|      1        |          R$ 6,00         |        R$ 7,00       |        R$ 8,00        |')
print('|      2        |          R$ 10,00        |        R$ 12,00      |        R$ 14,00       |')
print('|      3        |          R$ 14,00        |        R$ 17,00      |        R$ 20,00       |')
print('_-'*45)
while True:
#Entrada de dados pelo usuário
    sabor = input('Escolha um sabor [tr], [pr], [es]: ')
    #bloco condicional para sabor tradicional
    if sabor == 'tr':
        print("Sabor Tradicional selecionado.")
        quantidade = int(input("Digite quantas bolas de sorvete você quer: "))
        if quantidade == 1:
            valorTotal += 6.00
            print("Item foi adicionado ao pedido com sucesso.")
            fazerOutroPedido = str(input("Voce quer adicionar outro sorvete ao pedido? Digite [s] ou [n]: ")).strip().lower()
            if fazerOutroPedido == 's':
                continue
            else:
                break
        elif quantidade == 2:
            valorTotal += 10.00
            print("Item foi adicionado ao pedido com sucesso.")
            fazerOutroPedido = str(input("Voce quer adicionar outro sorvete ao pedido? Digite [s] ou [n]: ")).strip().lower()
            if fazerOutroPedido == 's':
                continue
            else:
                break
        elif quantidade == 3:
            valorTotal += 14.00
            print("Item foi adicionado ao pedido com sucesso.")
            fazerOutroPedido = str(input("Voce quer adicionar outro sorvete ao pedido? Digite [s] ou [n]: ")).strip().lower()
            if fazerOutroPedido == 's':
                continue
            else:
                break
        else:
            print("Quantidade informada é inválida, digite somente as opções informadas (1 | 2 | 3)!")
            continue
    #bloco condicional para sabor premium
    elif sabor == 'pr':
        print("Sabor Premium selecionado.")
        quantidade = int(input("Digite quantas bolas de sorvete você quer: "))
        if quantidade == 1:
            valorTotal += 7.00
            print("Item foi adicionado ao pedido com sucesso.")
            fazerOutroPedido = str(input("Voce quer adicionar outro sorvete ao pedido? Digite [s] ou [n]: ")).strip().lower()
            if fazerOutroPedido == 's':
                continue
            else:
                break
        elif quantidade == 2:
            valorTotal += 12.00
            print("Item foi adicionado ao pedido com sucesso.")
            fazerOutroPedido = str(input("Voce quer adicionar outro sorvete ao pedido? Digite [s] ou [n]: ")).strip().lower()
            if fazerOutroPedido == 's':
                continue
            else:
                break
        elif quantidade == 3:
            valorTotal += 17.00
            print("Item foi adicionado ao pedido com sucesso.")
            fazerOutroPedido = str(input("Voce quer adicionar outro sorvete ao pedido? Digite [s] ou [n]: ")).strip().lower()
            if fazerOutroPedido == 's':
                continue
            else:
                break
        else:
            print("Quantidade informada é inválida, digite somente as opções informadas (1 | 2 | 3)!")
            continue
    #bloco condicional para sabor especial
    elif sabor == 'es':
        print("Sabor Premium selecionado.")
        quantidade = int(input("Digite quantas bolas de sorvete você quer: "))
        if quantidade == 1:
            valorTotal += 8.00
            print("Item foi adicionado ao pedido com sucesso.")
            fazerOutroPedido = str(input("Voce quer adicionar outro sorvete ao pedido? Digite [s] ou [n]: ")).strip().lower()
            if fazerOutroPedido == 's':
                continue
            else:
                break
        elif quantidade == 2:
            valorTotal += 14.00
            print("Item foi adicionado ao pedido com sucesso.")
            fazerOutroPedido = str(input("Voce quer adicionar outro sorvete ao pedido? Digite [s] ou [n]: ")).strip().lower()
            if fazerOutroPedido == 's':
                continue
            else:
                break
        elif quantidade == 3:
            valorTotal += 20.00
            print("Item foi adicionado ao pedido com sucesso.")
            fazerOutroPedido = str(input("Voce quer adicionar outro sorvete ao pedido? Digite [s] ou [n]: ")).strip().lower()
            if fazerOutroPedido == 's':
                continue
            else:
                break
        else:
            print("Quantidade informada é inválida, digite somente as opções informadas (1 | 2 | 3)!")
            continue
    #bloco condicional para entrada inválida pelo usuário
    else:
        print("Operação inválida, digite corretamente o sabor selecionado.")
        continue
print(f"O valor total do pedido foi de R$ {valorTotal:.2f}")