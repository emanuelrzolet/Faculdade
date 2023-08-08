#Vamos praticar alguns exercícios de condicionais aninhadas.
#Exercício 4.1.1: Escreva um algoritmo em Python em que o usuário
#escolhe se ele quer comprar maçãs, laranjas ou bananas. Deverá ser
#apresentado na tela um menu com a opção 1 para maçã, 2 para laranja e 3 para
#banana.

print("_-_" * 20 + " LOjA DE FRUTAS " + "_-_" * 20)
print("Veja a lista de opções de frutas: ")
opcao = int(input("[1] - Maça\n[2] - Laranja\n[3] - Banana\nDigite a Opção desejada: "))
quantidade = int(input("Digite quantas frutas você quer comprar: "))
preco = 0
if opcao == 1:
    preco = quantidade * 2.30
elif opcao == 2:
    preco = quantidade * 3.60
elif opcao == 3:
    preco = quantidade * 1.85
else:
    print("Voce nao digitou uma opção valida!")

print(f"O valor total do pedido foi R$ {preco:.2f}")