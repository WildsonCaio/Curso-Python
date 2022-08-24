#RELAÇÃO DE AGREGAÇÃO, UM DOS DOIS TIPOS DE RELAÇAO DA ASSOCIAÇÃO
#exemplo de agregação: carros e rodas, ambos podem existir sem o outro, mas o carro não funciona direito sem as rodas

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    def inserirProdutos(self, produto):
        self.produtos.append(produto)
    def listaProduto(self):
        for produto in self.produtos:
            print(produto.nome,produto.valor)
    def somaTotal(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total
#Neste exemplo carrinho funciona sem produto mas não totalmente
#E Produto funciona totalmente sem precisar da classe Carrinho
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

carrinho = CarrinhoDeCompras()
p1 = Produto('camisa',50)
p2 = Produto('iPhone',5000)
p3 = Produto('Caneca1',15)

carrinho.inserirProdutos(p1)
carrinho.inserirProdutos(p1)
carrinho.inserirProdutos(p2)
carrinho.inserirProdutos(p3)

carrinho.listaProduto()
print(carrinho.somaTotal())