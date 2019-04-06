#este é um dicionário importante para agregar informações, adicionar dados e evitar de criar diversas variáveis

usuario = {
	'nome': input('Digite o seu nome'),
	'idade': input('Digite sua idade'),
	'email': input('Digite o seu email')
}

nome = usuario['nome']
print('Usuário {} Cadastrado com Sucesso'.format(usuario))

exit()

# print(usuario)

print(usuario['nome'])
print(type(usuario))

print(usuario['idade'])
print(type(usuario['idade']))