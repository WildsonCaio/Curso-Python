#ENCAPSULAMENTO (esconder partes do codigo para proteger a classe ou o codigo)
#Linguagens criadas para serem orientadas a objetos geralmente tem 3 palavras reservadas de privacidade
#São elas: public, protected, private (elas não existem no python, infelizmente)

from lib2to3.pytree import Base


class BaseDeDados:
    def __init__(self):
        self.__dados = {} #Esse dict é o coração da classe, tudo depende dele
    @property #Tira a necessidade de colocar os parenteses quando chama a funçao abaixo dele, nesse caso seria (bd.dados) sem a necessidade do parenteses
    def dados(self): #Agora temos acesso para vizualizar a variavel, nao alterar
        return self.__dados
    def inserirCliente(self, id, nome):
        if 'clientes'not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id:nome})
    def listaClientes(self):
        for id,nome in self.__dados['clientes'].items():
            print(id, nome)
    def apagaCliente(self,id):
        del self.__dados['clientes'][id]
bd = BaseDeDados()
#Se fizermos bd.__dados = 'Qualquer outra coisa' ira gera varios erros e n conseguiremos executar mais nenhuma funçao
bd.inserirCliente(1, 'Otavio')
bd.inserirCliente(2, 'Miranda')
bd.inserirCliente(3, 'Rose')
bd.listaClientes()
bd.apagaCliente(2)
bd.listaClientes()
print(bd.dados)


#Tudo em python é publico
#Entao como tornamos algo protected ou private em python?
#protected seria inserir UM underline '_' na frente, o python n recomenda usar
#ele fica 'privado' mas de maneira sutil
#ainda da pra acessar com por exemplo bd.__dados
#e o private seria como em python?
#private seria inserir DOIS underline '__' na frente, o python quase nega o acesso a essa variavel
#pra acessar uma variavel com 2 underlines seria assim: nomeDaInstancia._NomeDaClasse__nomeDaVariavel