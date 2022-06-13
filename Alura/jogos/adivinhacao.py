import random


def jogo_adivinhacao():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual é o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar ume número entre 1 e 100!")
            continue

        acerto = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acerto):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Você errou. Seu chute é maior que o número secreto")
            elif (menor):
                print("Você errou. Seu chute é menor que o número secreto")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        if (rodada == total_de_tentativas):
            print("O número secreto era {}. Você fez um total de {} pontos".format(numero_secreto, pontos))

    print("Fim de jogo")


if __name__ == "__main__":
    jogo_adivinhacao()