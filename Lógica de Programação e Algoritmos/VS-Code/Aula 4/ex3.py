totalIdade = quantIngressos = idade = dinheiro = 0

while True:
    idade = input("Digite sua idade: ")
    if idade == "sair":
        break
    else:
        idade = int(idade)
        if idade < 3:
            print("Ingresso gratuito! ")
            totalIdade += idade
            quantIngressos += 1
        elif idade >= 3 and idade <= 12:
            print("O ingresso custará R$ 15,00")
            totalIdade += idade
            quantIngressos += 1
            dinheiro += 15
        elif idade > 12:
            print("O ingresso custará R$ 30,00")
            quantIngressos += 1
            totalIdade += idade
            dinheiro += 30
print(f"Foram vendidos {quantIngressos} ingressos e R$ {dinheiro} foram faturados.")
print(f"A media de idade é {totalIdade / quantIngressos}")