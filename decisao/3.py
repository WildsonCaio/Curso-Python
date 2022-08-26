m = str ("M")
f = str ("F")

sexo = str (input("Insira seu sexo (M ou F). "))

if sexo == m:
    print ("sexo masculino")
    
elif sexo == f:
    print ("sexo feminino")
    
elif sexo != f and sexo != m:
    print ("sexo invalido")
