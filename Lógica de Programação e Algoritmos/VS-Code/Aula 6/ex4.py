import datetime
pessoas = []
mulheresMenores30 = []
homensMaiores = []
idadeTotal = 0
anoAtual = datetime.date.today().year
while True:
    print('Cadastro de pessoas')
    nome = input('Nome: ')
    anoNascimento = int(input('Ano de Nascimento: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    pessoa = {'nome':nome, 'anoDeNascimento': anoNascimento, 'sexo': sexo}
    opção = input("Quer cadastrar outra pessoa? [S/N]: ").strip().upper()
    pessoas.append(pessoa)
    idade = (anoAtual - pessoa['anoDeNascimento'])
    idadeTotal += idade
    if idade < 30 and pessoa['sexo'] == 'F':
        mulheresMenores30.append(pessoa['nome'])

    pessoa.clear()
    if opção in 'N':
        print("Cadastro encerrado!")
        break
media = idadeTotal/len(pessoas)
print(f"O total de pessoas cadastradas foi {len(pessoas)}")
print(f"A media de idade é {media}")
print(f"A lista de mulheres com menos de 30 anos: \n{mulheresMenores30}")
for c in pessoas:
    print(c)
    #if c['sexo'] and (anoAtual - c['anoDeNascimento'] > media):
    #    homensMaiores.append(c['nome'])
#print(f"A lista de homens com idade acima da média é: {homensMaiores}")