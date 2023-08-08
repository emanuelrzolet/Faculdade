print("Seja bem vindo! Você está na loja de Emanuel Rosa Zolet.")
#Entrada de informações digitadas pelo usuário.
valor = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
#Variáveis para cálculo do valor total e do desconto.
valorTotal = valor * quantidade
valorComDesconto = 0
#Blocos de estrutura condicional
if quantidade < 200:
    print("Você não receberá desconto.")
    valorComDesconto = valorTotal
elif quantidade >= 200 and quantidade < 1000:
    print("Você ganhou um desconto de 5%.")
    valorComDesconto = valorTotal - (valorTotal * (5 / 100))
elif quantidade >= 1000 and quantidade < 2000:
    print("Você ganhou um desconto de 10%.")
    valorComDesconto = valorTotal - (valorTotal * (10 / 100))
else:
    print("Você ganhou um desconto de 15%.")
    valorComDesconto = valorTotal - (valorTotal * (15 / 100))
#Saída dos valores com e sem desconto para o terminal.
print(f"O valor SEM desconto é: R$ {valorTotal:.2f}")
print(f"O valor COM desconto é: R$ {valorComDesconto:.2f}")