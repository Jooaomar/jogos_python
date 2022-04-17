import random   #importando biblioteca. O 'random' não faz parte da biblioteca padrão python

def jogar():

    print('******************')
    print('Bem vindo ao Jogo Adivinha.')
    print('******************')

    numero_secreto = random.randrange(1, 101)    #gerando número aleatorio entre 1 e 100. Consulte as bibliotecas. Aqui é biblioteca 'random'
    #A biblioteca random é bem previsivel. Para gerar numeros seguros use 'secrets'
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):      #aplicando função 'range'. Nessa função colocamos '1' como valor
        # incial, o loop acaba com o valor do segundo campo que é valor de 'total_de_tentativas' + 1= 4. O '+1' foi colocado
        # porque as tentativas acabam sempre como o valor do segundo campo -1. Ex: (1, 3)'veja, começa com 1 e acaba com 2'.

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)  #transformando o script(texto) em um int(inteiro)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número de 1 a 100!")
            continue   #interrompendo não imprimindo o valor, mas sem quebrar o loop continuando as tentativas. Diferente do 'break'.

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print(f"Você acertou e fez {pontos} pontos!")  #interpolação de strings( colocando valores de variáveis nas strings
            break #saindo do loop
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")

if(__name__ == "__main__"):  #Se executar-mos esse jogo diretamente como programa principal. chamar variável 'chamar()'
    jogar()
