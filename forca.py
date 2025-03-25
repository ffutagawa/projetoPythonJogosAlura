
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

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.lower() == letra.lower()):
                    letras_acertadas [index] = letra
                index = index + 1
        else:
            erros = erros + 1        
        enforcou = erros == 6
        print(letras_acertadas)

        print("Fim jogo..")   

if(__name__ == "__main__"):
    jogar()

