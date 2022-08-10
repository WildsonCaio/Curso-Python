
nome = str (input("Crie seu usuario: "))
senha = str (input("Crie sua senha: "))

#abre ou criar com sobreescrever
data=open('nome.txt','a')
#escreve
data.write(f"{nome}\n")

data=open('senha.txt','a')
data.write(f'{senha}\n')
