class Retangulo:
    def __init__(self,comprimento,largura):
     
        self.comprimento=comprimento
        self.largura=largura

    def calcular_area(self):
            self.comprimento=float(input("Insira comprimento: "))
            self.largura=float(input("Insira largura: "))
            area= self.largura*self.largura
            return (f"A area é: {area} seu comprimento é {self.comprimento} e sua largura é {self.largura}")
            
Retangulo_1=Retangulo('comprimento','largura')
print (Retangulo_1.calcular_area())


