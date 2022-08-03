nota=float(input("INSIRA UMA NOTA entre 0 e 10: "))
if nota>=0 and nota<=10:
        print (f"{nota} é uma nota válida.")

while ((nota<0) or (nota>10)):
    nota=float(input("INSIRA UMA NOTA entre 0 e 10: "))
    if nota>=0 and nota<=10:
        print (f"{nota} é uma nota válida.")
        break