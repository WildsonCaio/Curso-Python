import random
listaforca = ["azul", "bicicleta", "tatu", "arvore","caminho"] #talvez adicionar menu de adicionar
palavra = random.choice(listaforca) #Escolhe a palavra da lista aleatoriamente.
alfabeto = list("abdcefghijklmnopqrstuvwxyz") #list()retorna uma lista.
letrausada = []
tentativa = 6 #Quantidades de tentativas para acertar a palavra, fazer input tambem
#print(palavra)#Quero ver qual palavra o choice está escolhendo

while True:#loop para adicionar palavras para brincar
    addpalavra=str(input("Insira palavra para incluir em palavra ou JOGAR para jogar: "))
    listaforca.append(addpalavra)
    if addpalavra=="JOGAR":
    	break

while True: #condição de loop até condição parar
    
	print(f"\nVocê usou as letras: {letrausada}")
	print(f"\nChances: {tentativa}")

	for i in palavra:
		if i in letrausada:#mostrar a palavra mascarada e revelar após acerto
			print(i, end="")#end para não quebrar linha
		#if letrausada in listaforca:
			#break
		else:
			print('_',end="")#end para não quebrar linha

	chute = input("\n\nInsira letra MINÚSCULA ou 'SAIR' para encerrar o jogo: ")
	if chute in letrausada:
		print("Você já usou essa letra")
	letrausada.append(chute)

	if tentativa == 1:
			print(f"A palavra era: {palavra}")
			break

	if chute == "SAIR":
		break	
	elif chute not in alfabeto or chute == '':
		print("Insira letra tipo: abdcefghijklmnopqrstuvwxyz")

	if chute in palavra:
		print(f"POSSUI LETRA: {chute}")
	else:
		print(f"NÃO TEM LETRA: {chute}")
		tentativa -=1