
class Pessoa:
    def __init__(self,nome,vida,energia,mana,fome):
        self.__nome = nome
        self.__vida = vida
        self.__energia = energia
        self.__mana = mana
        self.__fome = fome

    @property
    def nome(self):
        return self.__nome


    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self,vida):
            self.__vida=vida
    def tomarDano(self):
        self.vida-=15

        
    @property
    def energia(self):
        return self.__energia
    @energia.setter
    def energia(self,energia):
            self.__energia=energia
    def perderEnergia(self):
        self.energia-=10
        

    @property
    def mana(self):
        return self.__mana
    @mana.setter
    def energia(self,mana):
            self.__mana=mana
    def perderMana(self):
        self.mana-=10
        

    @property
    def fome(self):
        return self.__fome
    @fome.setter
    def fome(self,fome):
        self.__fome=fome
    def ganharFome(self):
        self.fome+=5


Nome_1=Pessoa("TESTE",100,50,100,100)
print (Nome_1.vida)
print (Nome_1.nome)

Nome_1.tomarDano()
print (Nome_1.vida)
        