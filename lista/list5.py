numero = [1,2,3,4,5,6,7,8,9,10]
par=[]
imp=[]
for item in numero:
    if item%2:
        imp.append(item)
    
    else:
        par.append(item)

print()
print (f"Numeros impares: {imp}")
print()
print (f"Numeros pares: {par}")