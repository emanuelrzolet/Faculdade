#Exercício 2
#19
#21
#Escreva um algoritmo que leia dois valores
#numéricos e que pergunte ao usuário qual
#operação ele deseja realizar: adição (+),
#subtração (-), multiplicação (*) ou divisão
#(/). Exiba na tela o resultado da operação
#desejada (exercício da apostila – aula 3)

n1 = float(input("Digite o valor do primeiro numero: "))
n2 = float(input("Digite o valor do segundo numero: "))

print("Voce quer fazer qual operação?")
print("Opçoes:\n[+]\n[-]\n[*]\n[/]")
opcao = input("Digite a opcao desejada: ")
if opcao == "+":
    print(f"O resultado é: {n1 + n2}")
elif opcao == '-':
    print(f"O resultado é: {n1 - n2}")
elif opcao == '*':
    print(f"O resultado é: {n1 * n2}")
elif opcao == '/':
    print(f"O resultado é: {n1 / n2}")