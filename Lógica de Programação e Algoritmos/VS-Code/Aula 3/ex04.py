#Exercício 3.3.2: Escreva um algoritmo que lê um valor inteiro qualquer.
#Após, verifique se este valor está contido dentro dos seguintes intervalos: -100 x
#< -1 e 1 < x < 100. Imprima na tela uma mensagem caso ele esteja em um dos
#intervalos.

v = int(input("Digite um valor inteiro: "))
if v > -100 and v < -1 or v < 100:
    print("Foi atingido")
