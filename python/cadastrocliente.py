listacliente=[]
emailcliente=[]
listaproduto=[]
valorproduto=[]


while True:
        #ler produtos ou clientes no .txt
        menu=str(input("Você quer ver cadastros, cadastrar ou SAIR: "))
        if menu=="SAIR":
                break
        elif menu=="ver":
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
                                

        elif menu=="cadastrar":
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