class Bomba_Combustivel:
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.tipodeCombustivel=tipoCombustivel
        self.valorLitro=valorLitro
        self.quantidadeCombustivel=quantidadeCombustivel 

    def combustivel(self,combustivel):
        self.tipodeCombustivel=combustivel

    def preco(self,preco):
        self.valorLitro=preco

    def litro(self,litros):
        self.quantidadeCombustivel=litros

mostrarcombustivel=Bomba_Combustivel("etanol",10,150) #atribuindo combustivel,preço,quantidade
mostrarcombustivel.combustivel("gasolina")
print (mostrarcombustivel.combustivel()) #mostrar tipodeCombustivelClasse
