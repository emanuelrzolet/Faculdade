v = int(input("Digite um valor inteiro: "))
notas = 0
n100 = n50 = n20 = n10 = n5 = n1 = 0
while True:
    notas += 1
    if v >= 100:
        v -= 100
        n100 += 1
        print(v)
        continue
    elif v >= 50:
        v -= 50
        n50 += 1
        print(v)
        continue
    elif v >= 20:
        v -= 20
        n20 += 1
        print(v)
        continue
    elif v >= 10:
        v -= 10
        n10 +=1
        print(v)
        continue
    elif v >= 5:
        v -= 5
        n5 += 1
        print(v)
        continue
    elif v >= 1:
        v -= 1
        n1 += 1
        print(v)
        continue
    elif v == 0:
        print(f"O valor chegou a {v}, foram usadas {notas} notas e delas foram: ")
        print(f"{n100} - 100\n{n50} - 50\n{n20} - 20,\n{n10} - 10\n{n5} - 5\n{n1} - 1")
        break
    else:
        print("Algo deu errado")