# Para a liberação de um financiamento imobiliário, uma construtora exige que a
# renda mensal líquida mínima seja maior ou igual a R$ 8.500,00 e que o total de
# comprometimento com outros financiamentos ou empréstimos não ultrapasse 20%
# da renda mensal líquida. Utilizando o Python, faça um programa que informe se o
# financiamento será liberado ou não com base na renda mensal líquida e no total de
# outros financiamentos ou empréstimos por parte do cliente.
rendaDeclarada = float(input("Digite sua renda mensal liquida: "))
valorFinanciamento = float(input("Digite o valor a financiar incluindo outros financiamentos: "))
renda = 8500.00
if rendaDeclarada >= 8500 and (valorFinanciamento * 0.20) < rendaDeclarada:
    print("Financiamentoa provado!")
else: print("Financiamento recusado!")
    
