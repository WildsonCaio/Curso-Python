from audioop import reverse


lista=[]
while True:
    
    numero=float(input("INSIRA numeros: "))
    if numero==0:
        break
    lista.append(numero)
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)