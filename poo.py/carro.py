class Carro:
    def __init__(self,monobloco,rodas,motor,cambio):
        self.monobloco = monobloco
        self.rodas = rodas
        self.motor = motor
        self.cambio = cambio

Carro_1=Carro('hach','aço 1020','1.0','5 marchas')


print (Carro_1.monobloco)
print (Carro_1.rodas)
print (Carro_1.motor)
print (Carro_1.cambio)