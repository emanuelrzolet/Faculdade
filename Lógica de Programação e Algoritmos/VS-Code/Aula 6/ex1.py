notas = [9,10,5,7,6,2,8,9,4,1,2,4,5,2,8,7,3,1,0]
maior = total = quantnotas = 0
for i in notas:
    if quantnotas == 0:
        maior = i
    quantnotas += 1
    if i > maior:
        maior = i
    total += i
media = total / quantnotas
listaOrdenada = sorted(notas)
print(f"{maior} maior nota\n{media}Media\n{listaOrdenada}")