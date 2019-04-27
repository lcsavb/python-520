# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message# of congratulations to the winner, and ask if the
# players want to start a new game)


def verificar_entrada(entrada_jogador):
    if entrada_jogador == 'pedra':
        return True
    elif entrada_jogador == 'tesoura':
        return True
    elif entrada_jogador == 'papel':
        return True
    else:
        return False


def jogadas_do_1():
    entrada_jogador_1 = input('Jogador 1: Pedra, tesoura ou papel? \n')
    while not verificar_entrada(entrada_jogador_1):
        print('Jogador 1, você é burro! Tente digitar certo!')
        entrada_jogador_1 = input('Jogador 1: Pedra, tesoura ou papel? \n')
    return entrada_jogador_1

#duas funções para as jogadas não são necessárias!

def jogadas_do_2():
    entrada_jogador_2 = input('Jogador 2: Pedra, tesoura ou papel? \n')
    while not verificar_entrada(entrada_jogador_2):
        print('Jogador 2, você é burro! Tente digitar certo!')
        entrada_jogador_2 = input('Jogador 2: Pedra, tesoura ou papel? \n')
    return entrada_jogador_2


print('Pedra/Tesoura/Papel \n')


x = jogadas_do_2()
y = jogadas_do_2()


if x == y:
    print('EMPATE, ANIMAIS!')
if x.lower() == 'pedra' and y.lower() == 'tesoura':
    print('JOGADOR 1 VENCEU!')
elif x.lower() == 'tesoura' and y.lower() == 'papel':
    print('JOGADOR 1 VENCEU!')
elif x.lower() == 'papel' and y.lower() == 'pedra':
    print('JOGADOR 1 VENCEU!')

else:
    print('JOGADOR 2 VENCEU!')


# como continuar jogando sem encerrar o programa?