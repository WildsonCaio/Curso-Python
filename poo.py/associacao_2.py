#RELAÇÃO DE ASSOCIAÇÃO, UMA CLASSE NÃO DEPENDE DA OUTRA PARA EXISTIR
class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None
    @property
    def nome(self):
        return self.__nome 
    @property
    def ferramenta(self):
        return self.__ferramenta
    @ferramenta.setter
    def ferramenta(self, objeto):
        self.__ferramenta = objeto
class Caneta:
    def __init__(self, marca):
        self.__marca = marca
    @property
    def marca(self):
        return self.__marca
    def escrever(self):
        print('Caneta está escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está escrevendo...')



escritor = Escritor('Joao')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
escritor.ferramenta = caneta #ferramenta esta recebendo o objeto da classe inteira para a variavel ferramenta
escritor.ferramenta.escrever() 
escritor.ferramenta = maquina
escritor.ferramenta.escrever() 