class Conta_bancaria:
    def __init__(self,cliente,conta,saldo):
            
        self.cliente=cliente
        self.conta=conta
        self.saldo=saldo  

    def depositar(self,deposito):
        self.saldo+=deposito

    def sacar(self,deposito):
        self.saldo-=deposito


class ContaPoupanca(Conta_bancaria):
    def __init__(self, cliente, conta, saldo):
        super().__init__(cliente, conta, saldo)

    def rendimento_do_dia(self):
        self.saldo+=self.saldo*0.10
        

    
add_cliente= ContaPoupanca ("João","001",50) # inserir clinete
print (add_cliente.cliente) #mostrar cliente
print (add_cliente.conta) # mostrar conta
print (add_cliente.saldo) #mostrar saldo
add_cliente.depositar(112) #usa variavel cliente,usando função depositar com valor dentro de parenteses
add_cliente.sacar(12) #usa variavel cliente,usando função sacar com valor dentro de parenteses
print (add_cliente.saldo)
add_cliente.rendimento_do_dia()
print (add_cliente.saldo)

