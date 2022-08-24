#classes abstratas sao classes que n queremos que seja instaciada
#pode ter metodos concretos(normais) e tambem metodos abstratos(n tem corpo/código, 
#mas as classes filhas sao obrigadas a criar esse método em sua estrutura)
from abc import ABC, abstractmethod

# class A(ABC):
#     @abstractmethod
#     def falar(self):
#         pass
# class B(A):
#     def falar(self):
#         print('Falando....B')

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
    @property
    def agencia(self):
        return self._agencia
    @property
    def conta(self):
        return self._conta
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int,float)):
            raise ValueError("Saldo precisa ser numerico")
        self._saldo = valor
    def depositar(self,valor):
        if not isinstance(valor, (int,float)):
            raise ValueError("Valor de deposito precisa ser numerico")
        self.saldo += valor
        self.detalhes()
    def detalhes(self):
        print(f'Agencia: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')
    @abstractmethod
    def sacar(self,valor):
        pass
class Poupanca(Conta):
    def sacar(self,valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
            return
        self.saldo -= valor
        self.detalhes()
class Corrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite
    @property
    def limite(self):
        return self._limite
    def sacar(self,valor):
        if (self.saldo+self.limite) < valor:
            print("Saldo insuficiente")
            return
        self.saldo -= valor
        self.detalhes()
cp = Poupanca(1111,2222,0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)
print("####")
cc = Corrente(1111,3333,0,500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
#conta = Conta(1111,2222,0)