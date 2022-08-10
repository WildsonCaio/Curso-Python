
cadastrocliente=str(input("Você quer visualizar cadastro de clientes de produtos ou clientes"))
        
if cadastrocliente=="produtos":
        #leitura do txt
        data=open('listaproduto.txt','r')
        data.read('listaproduto.txt')
        print('listaproduto.txt')

elif cadastrocliente=="clientes: ":               
        #leitura do txt
        data=open('listacliente.txt','r')
        data.read('listacliente.txt')
