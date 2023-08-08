#Exercício 4.1.2 (adaptado de Puga, p. 48): Faça um algoritmo que receba três
#valores, representando os lados de um triângulo fornecidos pelo usuário.
#Verifique se os valores formam um triângulo e classifique como:
#a) Equilátero (três lados iguais);
#b) Isósceles (dois lados iguais);
#c) Escaleno (três lados diferentes).
#Lembre-se de que, para formar um triangulo, nenhum dos lados pode ser igual
#a zero e um lado não pode ser maior do que a soma dos outros dois.

a = int(input("Digite o valor do lado 1: "))
b = int(input("Digite o valor do lado 2: "))
c = int(input("Digite o valor do lado 3: "))

if (b - c) < a < b + c or (a - c) < b < a + c or (a - b) < c < a + b:
    print("É possivel formar um triangulo.")
    if a == b and b == c and a == c:
        print("O triangulo é equilatero.")
    elif a != b and b != c and a != c:
        print("O triangulo é escaleno.")
    else:
        print("O triangulo é Isosceles")
else:
    print("Não é possivel formar um triangulo.")

