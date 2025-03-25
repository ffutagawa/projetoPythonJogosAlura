
def jogar():
    print("**JOGO DE FORCA**")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_",]

    enforcou  = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input("Informe uma letra: ")
        chute = chute.strip()

        index = 0
        ##for letra in palavra_secreta:
        for letra in palavra_secreta:
            if(chute.lower() == letra.lower()):
                letras_acertadas [index] = letra
            index = index + 1

        print(letras_acertadas)

        print("jogando..")   

if(__name__ == "__main__"):
    jogar()

