
def jogar():
    print("**JOGO DE FORCA**")

    palavra_secreta = "banana"
    enforcou  = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Informe uma letra: ")
        chute = chute.strip()


        index = 0
        ##for letra in palavra_secreta:
        for index, letra in enumerate(palavra_secreta):
            if(chute.lower() == letra.lower()):
                print(f"Encontrei a letra {letra} na posição {index + 1}")
            index = index + 1
        print("jogando..")   

if(__name__ == "__main__"):
    jogar()

