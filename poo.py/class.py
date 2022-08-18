

class Celular:
    def __init__(self,camera,memoria,bateria,modelo):
        self.camera = camera
        self.memoria = memoria
        self.bateria = bateria
        self.modelo = modelo

Celular1=Celular('50mpx','2gb','3000mah','lgk10')

print (Celular1.camera)
