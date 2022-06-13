def jogo_forca():
    print("********************************")
    print("***Bem vindo ao jogo de forca***")
    print("********************************")

    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 6


    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:

            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1

        else:
            tentativas -= 1
        enforcou = tentativas == 0
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if (acertou):
        print("Parabéns! Você acertou a palavra secreta!")
    else:
        print("Você foi enforcado! A palavra secreta era {}".format(palavra_secreta))


if (__name__ == "__main__"):
    jogo_forca()
