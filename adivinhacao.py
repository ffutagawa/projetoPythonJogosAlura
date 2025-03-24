import random

def jogar():
    print("**JOGO DE ADIVINHACAO**")

    numero_secreto = round(random.randrange(1, 10))
    tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1)Facil (2)Medio (3)Dificil")
    nivel = int(input("Defina um nivel: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    print("aaaqui", numero_secreto)

    while (rodada <= tentativas):
        print("Tentativa: {} / {}".format(rodada, tentativas))
        meu_numero = int(input("Digite o seu numero entre 1 e 100: "))

        if (meu_numero < 1 or meu_numero > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = meu_numero == numero_secreto
        maior = meu_numero > numero_secreto
        menor = meu_numero < numero_secreto

        if (acertou):
            print("acertou fez {}".format(pontos),"O meu número: ", meu_numero)
            break
        else:
            if(maior):
                print("Seu número foi MAIOR que o número secreto")
            elif(menor):
                print("Seu número foi MENOR que o número secreto") 

            pontos_perdidos = abs(numero_secreto - meu_numero)
            pontos = pontos - pontos_perdidos    
        rodada = rodada + 1

        if rodada == 0:
            print("Fim das tentativas! O número secreto era", numero_secreto)

if(__name__ == "__main__"):
    jogar()
