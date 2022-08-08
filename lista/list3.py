lista=[]
for i in range(0,4):
    numero=float (input("Insira nota: "))
    lista.append(numero)
soma=sum(lista)
print (f"As notas são {lista}")
print (f"As notas sãoA média é {(soma/4)}")