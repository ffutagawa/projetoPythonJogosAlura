import adivinhacao
import forca

def escolha_jogo():
    print("*******Escolha o seu jogo!*******")

    print("(1) Forca (2) Adininhação")

    jogo = int(input("Qual Jogo?"))

    if( jogo == 1):
        print ("Jogo forca")
        forca.jogar()
    elif(jogo ==2):
        print("Jogo Adivinhacao")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()