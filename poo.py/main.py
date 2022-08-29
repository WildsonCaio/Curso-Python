from aaaa import ContaEspecial,ContaPoupanca
nome = input("Qual o seu nome?\n")
opc = int(input("Qual conta deseja criar? \n 1-Conta Corrente\n2-Conta Poupança\n3-Sair\n"))
match opc:
    case 1:
        cliente = ContaEspecial(nome,148072,0,500)
        print(cliente.saldo)
        dinheiro = float(input("Quanto deseja depositar?\n"))
        cliente.depositar(dinheiro)
        print(cliente.saldo)
        dinheiro = float(input("Quanto deseja sacar?\n"))
        cliente.sacar(dinheiro)
        print(cliente.saldo)
    case 2:
        cliente = ContaPoupanca(nome,151012,0,10)
        print(cliente.saldo)
        dinheiro = float(input("Quanto deseja depositar?\n"))
        cliente.depositar(dinheiro)
        print(cliente.saldo)
        dinheiro = float(input("Quanto deseja sacar?\n"))
        cliente.sacar(dinheiro)
        print(cliente.saldo)
        cliente.calcularNovoSaldo()
        print("Poupança rendendo")
        print(cliente.saldo)
    case 3:
        exit()
    case _:
        print("Opção Inválida")