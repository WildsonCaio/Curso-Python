class Usuario:
    def __init__(self,nome,email,idade,senha):
        self.nome=nome
        self.email=email
        self.idade=idade
        self.senha=senha

    def add_user(self):
        return("Usuario adicionado com sucesso!")

usuario_1 = Usuario ("joao","@hotmail","22","1234")

print(usuario_1.add_user())