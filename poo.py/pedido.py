class Pedido:

    def __init__(self):
        self.listaPedido=[]

    def insereProduto(self,produto,quantidade):
        self.listaPedido.append(Item(produto,quantidade))

    def valortotal(self):
        for i in self.listaPedido:
           
            print (linha())
            print(
            f'Produto: {i.produto.nomeproduto}'
            f'\nPreço: {i.produto.valor}'
            f'\nCódigo: {i.produto.codigo} '
            f'\nQuantidade: {i.quantidade} '
            f'\nTotal: {(i.quantidade*i.produto.valor)} ')
            print (linha())
    

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
#insereProduto=Produto(input,input,input)

adicionar_produto=Pedido(input("Insira nome do produto: "),(input("Insira quantidade do produto: ")))
adicionar_produto.insereProduto(maca,5)
adicionar_produto.insereProduto(agua,3)
#

adicionar_produto.valortotal() #chama função listar que está em pedido