
escolha=int(input("Qual tabuada quer fazer: "))
print()
ini=int(input("Qual inicio: "))
print()
fim=int(input("Qual qual fim "))
print()
print(f"Montar a tabuada de: {escolha}")
print(f"Começar por: {ini}")
print(f"Terminar em: {fim}")
print()
print(f"Vou montar a tabuada de {escolha} começando em {ini} e terminando em {fim}")

for i in range(ini,fim+1):    
    print(f"{escolha} X {i} = {i*escolha}")