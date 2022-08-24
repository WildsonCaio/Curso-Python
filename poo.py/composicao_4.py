#COMPOSICAO: RELAÇÃO MAIS FORTE ENTRE CLASSES
#Uma classe vai ser dona de objetos de outras classes
#Se a classe principal for apagada todos os objetos q usam a classe principal
#serao apagadas
#Uma classe pertence a outra classe
#Nesse nosso exemplo, endereço é instaciado dentro da classe Cliente

from http import client


class Cliente:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    def insereEndereco(self,cidade,estado):
        self.enderecos.append(Endereco(cidade,estado))
    def listaEnderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade,endereco.estado)
    def __del__(self):
        print(f'{self.nome} FOI APAGADO')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')

cliente1 = Cliente('Bruno',21)
cliente1.insereEndereco('Palhoça','SC')
print(cliente1.nome)
cliente1.listaEnderecos()
print()
cliente2 = Cliente('Robson',56)
cliente2.insereEndereco('Salvador','BA')
cliente2.insereEndereco('Rio de Janeiro','RJ')
print(cliente2.nome)
cliente2.listaEnderecos()
del cliente2
print()
cliente3 = Cliente('João',18)
cliente3.insereEndereco('Curitiba','PR')
print(cliente3.nome)
cliente3 .listaEnderecos()

print('###############################################')