#Associação - Usa| Agregação - Tem| Composição - É dono| Herança é
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
#OQ TEM EM COMUM ENTRE ESSAS DUAS CLASSES? SAO PESSOAS!
class Aluno(Pessoa):#Esta herdando a classe pessoa
    def estudando(self): #Função somente do aluno
        print(f"{self.nomeclasse} está estudando")

c1 = Cliente('Rovéria',74)
a1 = Aluno('Enzo',11)

print(c1.nome)
print(a1.nome)
print("####")
c1.falar()
a1.falar()