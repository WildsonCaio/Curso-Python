listacliente=[]
emailcliente=[]
listaproduto=[]
valorproduto=[]



cadastrocliente=str(input("Você quer visualizar cadastro de clientes de produtos ou clientes: "))
if cadastrocliente=="produtos":
        #leitura do txt
        data=open('listaproduto.txt','r')
        data.read(listaproduto)
        print(listaproduto)

elif cadastrocliente=="clientes: ":               
        #leitura do txt
        data=open('listacliente.txt','r')
        data.read('listacliente.txt')

#inserir produtos e clientes no .txt
while True:
        cadastro=str(input("Você quer cadastrar produtos ou clientes ou SAIR: "))
        if cadastro=="SAIR":
                break
        while True:
                if cadastro=="produtos":
                        produto=str (input("Insira nome do produto ou SAIR: "))
                        if produto=="SAIR":
                                break
                        listaproduto.append(produto)

                        valor = float(input("Insira valor do produto: "))
                        #adiciona na lista
                        valorproduto.append(valor)

                        #salva produto no txt
                        data=open('listaproduto.txt','a')
                        data.write(f"{listaproduto},{valorproduto}\n")

                elif cadastro=="clientes":
                        cliente=str(input("Insira nome cliente: "))
                        if cliente=="SAIR":
                                break
                        listacliente.append(cliente)

                        email = str(input("Insira email do cliente: "))
                        emailcliente.append(email)
                        
                        #salva cliente no txt
                        data=open('listacliente.txt','a')
                        data.write(f"{listacliente},[{email}]\n")
