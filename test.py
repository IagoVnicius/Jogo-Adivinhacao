import random

print('*********************************************************************')
print('**************** Bem vindo ao jogo da adivinhação *******************')
print('*********************************************************************')

print('(1) Fácil, (2) Médio, (3) Difícil')
nivel = int(input('Escolha a dificuldade do jogo: '))
pontos = 1000


if (nivel == 1):
    total_de_tentativas = 20
    print('Você tem 20 tentativas.')
elif (nivel == 2):
        total_de_tentativas = 10
        print('Você tem 10 tentativas.')
else:
        total_de_tentativas = 5
        print('Você tem 5 tentativas.')

numero_secreto = random.randrange(1,101)


for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Escolha um número entre 1 e 100: '))

    acertou =   numero_secreto == chute
    maior =     numero_secreto > chute
    menor =     numero_secreto < chute

    if (chute > 100 or chute < 1):
        print('Você deve digitar um número entre 1 e 100')

    if (acertou):
        print('Você acertou !!!')
        break
    else:                                      # DICAS PARA O JOGADOR
        if(menor):
            print('O numero secreto é menor')
        elif (maior):
            print('O numero secreto é maior')
    total_de_pontos = abs((numero_secreto - chute))
    pontos = pontos - total_de_pontos

print('Fim de jogo, você fez um total de {} pontos'.format(pontos))