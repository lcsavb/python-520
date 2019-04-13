import json
import aleatorio as foo

def imprimir_bonito(obj):
	print(json.dumps(obj, indent=2))

def gerar_lista_usuarios(n):
	lista = []
	for i in range(n):
		u = foo.gerar_usuario_aleatorio()
		lista.append(u)
	return lista

lista_de_usuarios = gerar_lista_usuarios(100)

def gerar_csv(lista):
	TEMPLATE = '{};{};{};'
	for usuario in lista:
		usuario_formatado = TEMPLATE.format(
			usuario['nome'],
			usuario['email'],
			usuario['idade']
		)
		print(usuario_formatado)

#imprimir somente os usuários com mais de 30 anos

lista_usuarios_30 = []

for usuario in lista_de_usuarios:
	if usuario['idade'] > 30:
		lista_usuarios_30.append(usuario)

# imprimir_bonito(lista_usuarios_30)

emails_selecionados = []

print(len(lista_de_usuarios))

for usuario in lista_de_usuarios:
	if 'a' in usuario['email'].lower()  or 'd' in usuario['email'].lower():
		emails_selecionados.append(usuario)

gerar_csv(emails_selecionados)

print('main.py: {}'.format(__name__))