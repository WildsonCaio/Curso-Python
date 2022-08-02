import random

pc = random.randint(1,100)

tentativa = 5




while True:

    chute = int (input("Insira um número: \n"))

    if tentativa == 1:
        print(f"O número era: {pc}")
        break

    elif chute > pc:
        print ("O numero é MENOR")
        tentativa -=1

    elif chute < pc:
        print ("O numero é MAIOR")
        tentativa -=1
    
    elif chute == pc:
        print ("Você acertou!")
        print(pc)
        break

    
# jogo de acerto com dicas!

