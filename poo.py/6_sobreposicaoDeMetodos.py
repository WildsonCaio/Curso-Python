#Sobreposição de Metodos- Reescrever metodos ja existentes
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    def falar(self):
        print(f"{self.nomeclasse} Falando")
class Cliente(Pessoa):#Esta herdando a classe pessoa
    def comprando(self):#Função somente do cliente
        print(f"{self.nomeclasse} está comprando")
    def falar(self):
        print(f"{self.nomeclasse} estamos em cliente")

class ClienteVip(Cliente):
    def __init__(self, nome, sobrenome, idade): #Sobrepondo o construtor
        super().__init__(nome, idade)#Puxa o constrututor da classe acima
       #Pessoa.__init__(self,nome,idade) serve para puxar construtor especifico 
        self.sobrenome = sobrenome
    def falar(self):#esta sobrepondo o metodo falar da Classe Pessoa
        Pessoa.falar(self)#Chama o metodo de uma classe especifica
        Cliente.falar(self)#Chama o metodo de uma classe especifica
        super().falar()#executa o metodo da classe primeira classe acima a ter esse metodo
        print(f"{self.nome} {self.sobrenome} está Falando com Elegância")

c1 = Cliente('rosimeri',150)
c2 = ClienteVip('Alfred','LongTown', 50)

c1.falar()
c2.falar()