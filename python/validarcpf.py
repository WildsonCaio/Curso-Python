
n1=int (input(f"Insira o numero 1 do CPF: "))
n2=int (input(f"Insira o numero 2 do CPF: "))
n3=int (input(f"Insira o numero 3 do CPF: "))
n4=int (input(f"Insira o numero 4 do CPF: "))
n5=int (input(f"Insira o numero 5 do CPF: "))
n6=int (input(f"Insira o numero 6 do CPF: "))
n7=int (input(f"Insira o numero 7 do CPF: "))
n8=int (input(f"Insira o numero 8 do CPF: "))
n9=int (input(f"Insira o numero 9 do CPF: "))
n10=int (input(f"Insira o numero 10 do CPF: "))
n11=int (input(f"Insira o numero 11 do CPF: "))


vald1=((n1*10)+(n2*9)+(n3*8)+(n4*7)+(n5*6)+(n6*5)+(n7*4)+(n8*3)+(n9*2))

val1=((vald1*10)%11)
print(val1)

vald2=((n1*11)+(n2*10)+(n3*9)+(n4*8)+(n5*7)+(n6*6)+(n7*5)+(n8*4)+(n9*3)+(n10*2))

val2=((vald2*10)%11)
print(val2)

    
if val1==10 or val1==n10  and val2==n11 or val2==10:
    print("CPF VÁlido")
    
elif val1!=n10 and val2!=n11 or n1==n2==n3==n4==n5==n6==n7==n8==n9==n10==n11:
    print("CPF invalido")
    











