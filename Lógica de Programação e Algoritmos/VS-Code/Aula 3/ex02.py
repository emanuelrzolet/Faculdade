#Exercício 2.5.2 (adaptado de Puga, p. 44): uma empresa concedeu um
#bônus de 20% para todos seus funcionários com mais de 5 anos de empresa.
#Todos os outros que não se enquadram nessa categoria receberam uma
#bonificação de 10%, somente. Escreva um algoritmo que leia o salário do
#funcionário e seu tempo de empresa, e apresente a bonificação de cada
#funcionário na tela.

tempoDeEmpresa = int(input("Digite a quantos anos voce está na empresa: "))
salario = float(input("Digite o seu salário atual em R$: "))

if tempoDeEmpresa >= 5:
    print(f'Voce tem {tempoDeEmpresa} anos de empresa e receberá um aumento de 20% em seu salario, o valor correspondente é {salario * (20 / 100)}')
elif tempoDeEmpresa < 5:
    print(f'Voce tem {tempoDeEmpresa} anos de empresa e receberá um aumento de 10% em seu salario, o valor correspondente é {salario * (20 / 100)}')