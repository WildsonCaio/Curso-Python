
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
    def perderVida(self):
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


class Movimento:
    def __init__(self,andar, correr, parar,esconder):
        self.andar = andar
        self.correr = correr
        self.parar = parar
        self.esconder=esconder
        #Movimento_1=Movimento(1,2,3,4)
        if Movimento== "1"
            return ("Você está andando")
        

class Ataque:
    def __init__(self, chute, soco):
        self.chute=chute
        self.soco=soco


insira_nome=(input("Qual seu nome? "))

Nome_1=Pessoa(insira_nome,100,100,100,100)

        

Nome_1.perderVida()
print (Nome_1.nome)
print (Nome_1.vida)
        