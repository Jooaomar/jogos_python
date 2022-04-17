import forca
import adivinha

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhcão")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinha.jogar()
    print("Fim de jogo")

if(__name__ == "__main__"):
    escolhe_jogo()
