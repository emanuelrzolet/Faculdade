#Exigência de Código 1
def cachorro_peso():
    while True:
        try:
            peso = int(input("Digite o peso do cachorro: "))
            if peso >= 50 or peso <= 0:
                 print("Peso inválido, Digite o peso entre 0 e 50")
                 continue
            else:
                if peso < 3:
                    return 40
                elif peso >= 3 and peso < 10:
                    return 50
                elif peso >= 10 and peso < 30:
                    return 60
                elif peso >= 30 and peso < 50:
                    return 70
        except ValueError:
            print("Peso inválido, digite somente valores numéricos.")
            continue
#Exigência de Código 2
def cachorro_pelo():
    print("Tipo de pelagem\n[c] - Curto\n[m] - Médio\n[l] - Longo")
    while True:
        pelo = input("Digite o tipo de pelagem do animal: ").strip().lower()
        if pelo in "cml":
            if pelo == 'c':
                return 1
            elif pelo == 'm':
                return 1.5
            elif pelo == 'l':
                return 2
        else:
            print("Tipo de pelo inválido!")
            continue
#Exigência de Código 3
def cachorro_extra():
    valor = 0
    print("Serviço Extra")
    print("[1] - Cortar unhas.\n[2] - Escovar os Dentes.\n[3] - Limpar Orelhas.\n[0] - Não Quer Mais Nada.")
    while True:
        try:
            escolha = int(input("Digite a opção desejada: "))
            if escolha == 1:
                valor += 10
                continue
            elif escolha == 2:
                valor += 12
                continue
            elif escolha == 3:
                valor += 15
                continue
            elif escolha == 0:
                return valor
            else:
                print("Opção inválida!")
        except ValueError:
            print("Opção inválida, somente serão aceitos valores numéricos.")
            continue

#main
print("Bem vindos ao Pet Shop de Emanuel Rosa Zolet!")
#Calculo do valor é obtido a partir do retorno das 3 funções criadas
#Exigência de código 4
total = (cachorro_peso() * cachorro_pelo()) + cachorro_extra()

print(f"O total a pagar é R$ {total}")