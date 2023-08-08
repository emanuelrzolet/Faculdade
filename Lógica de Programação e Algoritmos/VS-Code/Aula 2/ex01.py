preco = float(input("Digite o valor do produto em R$: "))
desconto = float(input("Digite qual desconto será aplicado: "))
print(f"O valor do produto com desconto ficara R$ {preco - preco * (desconto / 100)}")