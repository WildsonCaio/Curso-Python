excesso=(50)
multa=(4)

peso=float(input("Qual peso do peixe?\n"))
if peso>excesso:
    print(f"Vai pagar {(multa*(peso-50))} de multa")
else:
    print("Não vai pagar multa.")