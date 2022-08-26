mb=float(input("Insira quantos MB tem o arquivo: "))
net=int(input("Insira a velocidade da internet em MB/s: "))
print(f"Vai demorar{mb/(net*60)} minutos para download.")