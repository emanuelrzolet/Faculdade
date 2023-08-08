tup = ("Amo",'Carneiro','Passaro','figo','maca','teste','Organizaçao','tiro','palavras','pioneiro')
vogais = []
for c in tup:
    for i in range(0,len(c)):
        if c[i] in 'AaEeIiOoUu':
            vogais.append(c[i])
    print(f"{c} - {vogais}")
    vogais.clear()