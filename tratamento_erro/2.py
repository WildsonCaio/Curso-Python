
try:
    print(x)
except ZeroDivisionError:
    print("Não é possivel dividir por 0")
except NameError:
    print("Variável não definida")
