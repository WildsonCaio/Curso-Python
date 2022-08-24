class Pedido:

    def __init__(self):
        self.listaPedido=[]

    def insereProduto(self,produto,quantidade):
        self.listaPedido.append(Item(produto,quantidade))

    def valortotal(self):
        for i in self.listaPedido:
            print (i.produto.nomeproduto,(i.quantidade*Produto.valor))
    

class Item:

    def __init__(self,produto,quantidade):
        self.produto=produto
        self.quantidade=quantidade
        

class Produto:

    def __init__(self,valor,codigo,nomeproduto):
        self.valor=valor
        self.codigo=codigo
        self.nomeproduto=nomeproduto

def linha():

    return('-'*40)

maca=Produto(2,"001",("Maça"))
agua=Produto(5,"002","Água")
coca=Produto(10,"003","Refrigerante")

tazo=Pedido()
tazo.insereProduto(maca,5)
tazo.insereProduto(agua,3)
tazo.insereProduto(coca,7)

tazo.valortotal() #chama função listar que está em pedido

print (linha())
print(
f'Produto: {tazo.listaPedido[0].produto.nomeproduto}'
f'\nPreço: {tazo.listaPedido[0].produto.valor}'
f'\nCódigo: {tazo.listaPedido[0].produto.codigo} '
f'\nQuantidade: {tazo.listaPedido[0].quantidade} '
f'\ntotal: {tazo.listaPedido[0].quantidade*tazo.listaPedido[0].produto.valor} ')
print (linha())
