lista=[]
for i in range(0,3):
    numero=float(input("INSIRA numeros: "))

    lista.append(numero)
    
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)