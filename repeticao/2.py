nome = str (input("Insira seu usuario "))
senha = str (input("Insira sua senha "))

if senha!=nome:
    print ("Cadastro liberado")
    print()
else:
    print ("Usuario e Senha devem ser diferentes")
    print()

while (nome==senha):
    nome = str (input("Insira seu usuario "))
    senha = str (input("Insira sua senha "))
    
    if (nome==senha):
        print ("Usuario e Senha devem ser diferentes")
        print()
    
    elif nome!=senha:
        print ("Cadastro liberado")
        print()
        break