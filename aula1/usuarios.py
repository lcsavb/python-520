
lista_de_usuarios=[]

for e in range(10):
	usuario = {
		'nome': input('Digite o seu nome: '),
		'idade': input('Digite sua idade: '),
		'email': input('Digite o seu email: ')
	}
	lista_de_usuarios.append(usuario)

for usuario in lista_de_usuarios:
	print(usuario['nome'])

#print (lista_de_usuarios[0])

