# Em uma determinada disciplina, para compor a nota, foram realizadas duas
# atividades práticas e uma prova objetiva. A primeira atividade prática corresponde a
# 20% da nota, a segunda atividade prática corresponde a 30% da nota e a prova
# objetiva corresponde a 50% da nota da disciplina. Sabendo que se o estudante
# obtiver nota inferior a 30 está reprovado, nota maior ou igual a 30 e menor do que
# 70 está em exame final e nota maior ou igual a 70 está aprovado, faça um programa
# em Python onde são informadas as notas obtidas nas duas atividades práticas e na
# prova objetiva e é informada a nota obtida na disciplina e o resultado (reprovado, em
# exame final ou aprovado). Considere a nota da disciplina com uma casa decimal.

notaPratica1 = float(input("Digite o valor da nota da atividade pratica 1: "))
notaPratica2 = float(input("Digite o valor da nota da atividade pratica 2: "))
notaProva = float(input("Digite o valor da nota da prova: "))

media = notaPratica1 * 0.20 + notaPratica2 * 0.30 + notaProva * 0.5
if (media >= 70):
    print("Aprovado!")
elif (media < 70 and media >= 30):
    print("Está em exame!")
else:
    print("Está reprovado!")