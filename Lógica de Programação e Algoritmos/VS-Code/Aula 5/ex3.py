def calcFatorial(n):
    """
    Função recebe como parametro o numero a ser fatorado.
    Retorna o fatorial de um número inteiro positivo.
    """
    print("Calculo de fatorial!")
    if n == 1 or n == 0:
        print(f"O fatorial de {n} é 1")
    else:
        for c in range(n -1,0,-1):
            print(f"{n} * {c} = {n*c}")
            n *= c
def validarDados():
    while True:
        n = int(input("Digite um número inteiro e positivo: "))
        if n >= 1:
            return n
        else:
            print("Valor ditado nao está em conformidade com o solicitado.")
            continue


calcFatorial(validarDados())
