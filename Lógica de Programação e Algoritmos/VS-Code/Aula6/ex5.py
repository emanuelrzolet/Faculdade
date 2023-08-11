nome = input('Digite o nome do aluno: ')
n1 = int(input('Digite a nota: '))
n2 = int(input('Digite a nota: '))
n3 = int(input('Digite a nota: '))
media = (n1 + n2 + n3) / 3
situação =''
if media >= 7:
    situação = 'Aprovado'
elif media <7 and media >= 5:
    situação = 'Em exame'
else:
    situação = 'Reprovado'
aluno = {'Nome': nome, 'Média': media, 'Situação':situação}
print(aluno)