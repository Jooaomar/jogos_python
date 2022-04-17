import random     #para trazer valores aleátorio primeiro importe a biblioteca


def jogar():
    mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = iniciar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = pede_chute()

        
        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7               ## enforcou = True
        acertou = "_" not in letras_acertadas  ## Parando jogo ao acertar

        print(letras_acertadas)

    if acertou:
        impreimr_mensagem_vencedor()
    else:
        imprimir_mensagem_perdedor(palavra_secreta)
    print("Fim de jogo")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print() 

def imprimir_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print("  \      XXX        /     ")
    print("   |      XXX       |       ")
    print("   |                |        ")
    print("   |   I I I I I I  |        ")
    print("   |   I         I  |        ")
    print("   \_              _/       ")
    print("     \_          _/         ")
    print("       \ _______/          ")

def impreimr_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_de_abertura():
    print('******************')
    print('Bem vindo ao Jogo Forca.')
    print('******************')

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")  # abrindo o arquivo texto
    palavras = []

    for linha in arquivo:
        linha = linha.strip()  # limpando a palavras('linha')
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))         # escolhendo numero aletorio entre 0 e o total de palavras na lista (len(palavras))
    palavra_secreta = palavras[numero].upper()          #'upper()'Resolvendo o problema do uso de letras maiúsculas não aceitar
    return palavra_secreta

def iniciar_letras_acertadas(palavra):
    return ["_" for letra in palavra]          # colocando quantidade de "_" de acordo com 'palavras_secreta' aleatória

def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()                        ## O valor sairá sem espaçamento. Vai limpar 'strip()'
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0                             # variável que recebe a posição da letra
    for letra in palavra_secreta:         # verificando a string 'banana', que é um índice por ser uma str
        if chute == letra:
            letras_acertadas[index] = letra    # na posição(index) substituirar por letra no lugar do espaço ("_")
        index += 1

if (__name__ == "__main__"):
    jogar()
