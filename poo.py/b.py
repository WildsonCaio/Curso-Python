import re


class BombaDeCombustivel:
    def __init__(self,tipo,valor,qtd) -> None:
        self.tipo = tipo
        self.valor = valor
        self.qtd = qtd
    def abastecerPorValor(self,dinheiro):
        abastecidoEmLitros = dinheiro/self.valor
        self.alterarQuantidadeCombustivel(-abastecidoEmLitros)
        return abastecidoEmLitros
    def abastecerPorLitro(self,litros):
        abastecidoEmDinheiro = litros*self.valor
        self.alterarQuantidadeCombustivel(-litros)
        return abastecidoEmDinheiro
    def alterarValor(self,novoValor):
        self.valor = novoValor
    def alterarCombustivel(self, novoGasosa):
        self.tipo = novoGasosa
    def alterarQuantidadeCombustivel(self,quantidade):
        self.qtd += quantidade

bomba = BombaDeCombustivel("Gasolina",5,1000)
print(bomba.qtd)
print(bomba.abastecerPorLitro(2))
print(bomba.abastecerPorValor(20))
print(bomba.qtd)