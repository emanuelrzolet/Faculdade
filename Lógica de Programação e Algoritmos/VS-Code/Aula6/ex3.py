import random
print("Jokenpoo!")
jogada = []
while True:
    JogadaPC = random.randint(1,3)
    jogadaJogador = int(input("Digite:\n[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n[0] - Sair\nSua opção:"))
    if jogadaJogador == 0:
        print("Jogo finalizado")
        break
    elif jogadaJogador == 1 and JogadaPC == 3:
        print("Você ganhou!")
        jogada.append(('Voce ganhou', 'pedra vs tesoura'))
    elif jogadaJogador == 2 and JogadaPC == 1:
        print("Você ganhou!")
        jogada.append(('Voce ganhou', 'papel vs pedra'))
    elif jogadaJogador == 3 and JogadaPC == 2:
        print("Você ganhou!")
        jogada.append(('Voce ganhou', 'tesoura vs papel'))
    elif jogadaJogador == 1 and JogadaPC == 2:
        print("Você perdeu!")
        jogada.append(('Voce perdeu', 'pedra vs papel'))
    elif jogadaJogador == 2 and JogadaPC == 3:
        print("Você perdeu!")
        jogada.append(('Voce perdeu', 'papel vs pedra'))
    elif jogadaJogador == 3 and JogadaPC == 1:
        print("Você perdeu!")
        jogada.append(('Voce perdeu', 'tesoura vs pedra'))
    elif jogadaJogador == JogadaPC:
        print('Empatou')
        jogada.append(('Empatou', 'X vs X'))
    print(jogada)
