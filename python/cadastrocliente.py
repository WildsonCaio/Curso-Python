listacliente=[]
emailcliente=[]
listaproduto=[]
valorproduto=[]



cadastro=str(input("Você quer cadastrar produtos ou clientes ou SAIR: "))
if cadastro=="produtos":
        produto=str (input("Insira nome do produto: "))
        listaproduto.append(produto)

        valor = float(input("Insira valor do produto: "))
        #adiciona na lista
        valorproduto.append(valor)

        #salva produto no txt
        data=open('listaproduto.txt','a')
        data.write(f"{listaproduto},{valorproduto}\n")

elif cadastro=="clientes":
        cliente=str(input("Insira nome cliente ou digite SAIR para encerrar: "))
        listacliente.append(cliente)

        email = str(input("Insira email do cliente: "))
        emailcliente.append(email)
        
        #salva cliente no txt
        data=open('listacliente.txt','a')
        data.write(f"{listacliente}, {email}\n")
