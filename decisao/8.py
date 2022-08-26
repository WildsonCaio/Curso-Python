def maior(x,y,z):
    max = x

    if y > max:
        max = y
    if z > max:
        max = z

    return max

def menor(x,y,z):
    min = x

    if y < min:
        min = y
    if z < min:
        min = z

    return min

def menu():
    x = float(input('Qual o preço do produto: '))
    y = float(input('Qual o preço do Segundo produto : '))
    z = float(input('Qual o preço do Terceiro produto: '))

    print("você deve comprar o produto de:", menor(x,y,z))
    print()
    
while True:
    menu()
