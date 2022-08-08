lista=[]

for i in range(0,10):
    numero=float (input("Insira numero: "))
    lista.append(numero)
lista.sort(reverse=True)
print(lista)