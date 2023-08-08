loja = {'cenoura':[100,0.99],'brocolis':[50, 3.99],'batata': [200, 0.49],'cebola':[75,1.10]}
pedido = 0
while True:
    print('LOJA HORTIFRUTI')
    for k,v in loja.items():
        print(f"{k.capitalize()} tem {v[0]} unidades em estoque e o Preço é R$ {v[1]}")
    opção = input("Digite o item para acrescentar ao pedido ou digite sair para encerrar: ")
    if opção.lower().strip() == 'sair':
        print(f"O valor total do seu pedido foi {pedido}")
        break
    if opção.strip().lower() in "cenoura":
        quantidade = int(input("Digite quantas voce quer encomendar: "))
        pedido += loja["cenoura"][1] * quantidade
        loja["cenoura"][0] -= quantidade
    if opção.strip().lower() in "brocolis":
        quantidade = int(input("Digite quantas voce quer encomendar: "))
        pedido += loja["brocolis"][1] * quantidade
        loja["brocolis"][0] -= quantidade
    if opção.strip().lower() in "batata":
        quantidade = int(input("Digite quantas voce quer encomendar: "))
        pedido += loja["batata"][1] * quantidade
        loja["batata"][0] -= quantidade
    if opção.strip().lower() in "cebola":
        quantidade = int(input("Digite quantas voce quer encomendar: "))
        pedido += loja["cebola"][1] * quantidade
        loja["cebola"][0] -= quantidade
    