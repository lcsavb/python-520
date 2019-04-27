def cadastrar_usuario():
    usuario = {
        'data_cadastro': datetime.datetime.now(),
        'nome': input('Digite o nome: \n'),
        'email': input('Digite o email: \n'),
        'idade': input('Digite a idade: \n')
    }
    return usuario


class Usuario:

    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def maior_de_idade(self):
        if self.idade > 18:
            return True
        return False
# melhor fazer uma classe separada para cadastro
#     def cadastrar(self):
#         self.nome = input('Digite o seu nome: ')
#         self.email = input('Digite o seu email: ')
#         self.idade = input('Digite a sua idade: ')


class Cadastrador:

    def cadastrar_usuario(self):
        nome = input('Digite o seu nome:')
        email = input('Digite o seu email:')
        idade = int(input('Digite a sua idade:'))

        return Usuario(nome, email, idade)


cadastrador = Cadastrador()

usuario = cadastrador.cadastrar_usuario()

print(usuario.maior_de_idade())