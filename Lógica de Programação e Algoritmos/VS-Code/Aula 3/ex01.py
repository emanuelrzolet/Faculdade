#Vamos praticar alguns exercícios de condicional simples e composta.
#Exercício 2.5.1: desenvolva um algoritmo que solicite o seu ano de
#nascimento e o ano atual. Calcule a sua idade e apresente na tela.
#14Para fins de simplificação, despreze o dia e o mês do ano. Após o cálculo,
#verifique se a idade é maior ou igual a 18 anos e apresente na tela uma
#mensagem informando que já é possível tirar a carteira de motorista caso seja
#de maior.
import datetime
anoDeNascimento = int(input('Digite o Ano que você nasceu: '))
anoAtual = datetime.date.today().year
idade = anoAtual - anoDeNascimento
if idade >= 18:
    print(f"Voce tem {idade} anos, ou seja, é maior de idade.")
else:
    print(f"Voce tem {idade} anos, ou seja, é menor de idade.")