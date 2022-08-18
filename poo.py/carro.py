

class Carro:
    def __init__(self,monobloco,rodas,motor,cambio):
        self.monobloco = monobloco
        self.rodas = rodas
        self.motor = motor
        self.cambio = cambio

Carro1=Carro('hach','aço 1020','1.0','5 marchas')


print (Carro1.monobloco)
print (Carro1.rodas)
print (Carro1.motor)
print (Carro1.cambio)
