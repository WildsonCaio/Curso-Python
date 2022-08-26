salario = float (input("Insira seu dia da semana Ex: 1-Domingo, 2- Segunda, etc. "))
match salario:
    case 1:
        print("Segunda")
    case 2:
        print("Terça")
    case 3:
        print("Quarta")
    case 4:
        print("Quinta")
    case 5:
        print("Sexta")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
if salario <1 or salario >7:
    print("Não é dia de semana!")