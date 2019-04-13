# def change_to_int(mensagem_de_cadastro,mensagem_de_erro):
# 	entrada_usuario = input(mensagem_de_cadastro)
# 	try:
# 		return int(entrada_usuario)
# 	except ValueError: 
# 		print('O valor deve ser um número')
# 		raise ValueError(erro)

# def conserto_erros_do_cadastro(entrada_usuario, mensagem_de_cadastro, mensagem_de_erro):
# 	entrada_valida = False
# 	while not entrada_valida:
# 		try:
# 			int(entrada_usuario)
# 		except:
# 			print(mensagem_de_erro)

import os
import datetime
import time
import random

def cadastrar_usuario():
	usuario = {
		'data_cadastro': datetime.datetime.now(),
		'nome': input('Digite o nome: \n'),
		'email': input('Digite o email: \n'),
		'idade': input('Digite a idade: \n')
	}
	return usuario

probabilidade = random.random()
if probabilidade < 0.1:
	cadastrar_usuario()
else:
	print('Opa, não deu sorte!')

exit()

# start_time = time.clock()
# time.sleep(10.0)
# print('Tempo gasto = {}'.format(time.clock() - start_time))

novo_usuario = cadastrar_usuario()
os.system('clear')

d = novo_usuario['data_cadastro']

print(d.strftime("%d de %B de %Y, %H:%M"))  




