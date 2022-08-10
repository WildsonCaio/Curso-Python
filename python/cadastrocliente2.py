
cadastrocliente=str(input("Você quer visualizar cadastro de clientes de produtos ou clientes: "))
        
if cadastrocliente=="produtos":
        #leitura do txt
        with open('listaproduto.txt','r') as listproduto:
                for i in listproduto:
                        print(listproduto.read())

elif cadastrocliente=="clientes":               
        #leitura do txt
        with open('listacliente.txt','r') as listcliente:
                for i in listcliente:
                        print(listcliente.read())
