# Em uma empresa, a entrada em um determinado setor é liberada após o
# funcionário digitar uma determinada senha. Sabendo que uma das senhas é 705080
# e que a outra senha é 999999, faça um programa em Python onde o usuário digita
# uma senha. Se a senha estiver correta, aparece a mensagem que a entrada está
# liberada. Caso contrário, a mensagem é de que a entrada não está autorizada



escolha = int(input("Digite a senha para entrar: "))
senhas = (999999, 705080)

if (escolha == senhas[0] or escolha == senhas[1]):
    print("Acesso liberado!")
else:
    print("Senha incorreta!")