kWh = int(input("Digite o valor me kWh consumido: "))
tipo = input("Qual o tipo de instalação?\n[R] - Residencial\n[I] - Industrial\n[C] - Comercio\nSua Opção: ").upper().strip()
if tipo == "R" and kWh <= 500:
    preco = 0.40
elif tipo == "R" and kWh > 500:
    preco = 0.65
elif tipo == "C" and kWh <= 1000:
    preco = 0.55
elif tipo == "C" and kWh > 1000:
    preco = 0.60
elif tipo == "I" and kWh <= 5000:
    preco = 0.55
elif tipo == "I" and kWh > 5000:
    preco = 0.60
else:
    print("Valores digitados estao incorretos!!")
print(f"O valor da conta de luz é R$ {kWh * preco}")