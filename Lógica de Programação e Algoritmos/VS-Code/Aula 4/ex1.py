n1 = int(input("digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

while True:
    resposta = input('Tabela de Operações:\n[+]\n[-]\n[*]\n[/]\n[sair]\nDigite a Opção desejada: ')
    if resposta == 'sair':
        print('Saindo do programa!')
        break