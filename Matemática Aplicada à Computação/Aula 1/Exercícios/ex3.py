# Em uma empresa, a entrada em um determinado setor é liberada após o
# funcionário digitar uma determinada senha. Sabendo que a senha é 705080, faça
# um programa em Python onde o usuário digita uma senha. Se a senha estiver
# correta, aparece a mensagem que a entrada está liberada. Caso contrário, a
# mensagem é de que a entrada não está autorizada


escolha = input("Digite a senha para entrar: ")
senha = 705080

if (escolha != senha):
    print("Senha incorreta!")
else:
    print("Acesso liberado!")