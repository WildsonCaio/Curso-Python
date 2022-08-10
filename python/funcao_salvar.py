
nome = str (input("Crie seu usuario: "))
senha = str (input("Crie sua senha: "))

data=open('nome.txt','a')
data.write(f"{nome}\n")

data=open('senha.txt','a')
data.write(f'{senha}\n')
