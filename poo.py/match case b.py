class Pedido:
    def __init__(self) -> None:
        self.total = 0
        self.items = []
    def adicionarItem(self,produto, quantidade):
        self.items.append(ItemPedido(produto,quantidade))
    def calcularTotal(self):
        for i in self.items:
            self.total += i.quantidade * i.produto.valor
        return self.total
class ItemPedido:
    def __init__(self, produto, quantidade) -> None:
        self.produto = produto
        self.quantidade = quantidade
class Produto:
    def __init__(self,codigo,valor,descricao) -> None:
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao
fraldaGeriatrica = Produto("001",60,"Fralda Geriatrica")
aguaDeBanho = Produto("666",15000,"Agua gostosas")
controle = Produto("002",20,"Controle Remoto")
pedido = Pedido()
pedido.adicionarItem(fraldaGeriatrica,10)
pedido.adicionarItem(aguaDeBanho,2)
pedido.adicionarItem(controle,1)

print(pedido.items[0].quantidade)
#print(pedido.calcularTotal())