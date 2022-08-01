n1=float(input("Digite o 1º número: "))
n2=float(input("Digite o 2º número:: "))
n3=float(input("Digite o 3º número: "))
if n1 > n2 > n3:
    print("Do maior para o menor:", n1,"-", n2,"-", n3)
elif n2 > n1 > n3:
    print("Do maior para o menor:", {n2,"-", n1,"-", n3})
elif n3 > n2 > n1:
    print("Do maior para o menor:", {n3,"-", n2,"-", n1})
elif (n1 == n2 == n3) or (n2 == n1 == n3) or (n3 == n2 == n1):
    print("Números iguais!")