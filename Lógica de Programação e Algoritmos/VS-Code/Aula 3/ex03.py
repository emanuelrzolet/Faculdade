#Exercício 3.3.1 (adaptado de Menezes, p. 60): Um aluno, para passar de
#ano, precisa estar aprovado em todas as matérias que ele está cursando.
#Assuma que a média para aprovação é a partir de 7, e que o aluno cursa
#3 matérias, somente. Escreva um algoritmo que leia a nota final do aluno em
#cada matéria, e informe na tela se ele passou de ano ou não.

nota1 = float(input("Escreva a nota final da primeira materia: "))
nota2 = float(input("Escreva a nota final da segunda materia: "))
nota3 = float(input("Escreva a nota final da terceira materia: "))

if nota1 > 7 and nota2 >7 and nota3 >7:
    print("Voce atingiu a media 7 em todas as matérias. Voce foi aprovado!")
else:
    print("Você nao atingiu a média, Esta Reprovado!!!")