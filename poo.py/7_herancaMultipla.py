class A:
    def falar(self):
        print('Falando...A')
class B(A):
    def falar(self):
        print('Falando...B')
class C(A):
    def falar(self):
        print('Falando...C') 
class D(B,C):#procura os metodos falar() da esquerda pra direita,primeiro nela mesma dps em B dps em C
    pass

d = D()
d.falar()

