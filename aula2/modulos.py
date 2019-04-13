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

start_time = time.clock()
time.sleep(10.0)
print('Tempo gasto = {}'.format(time.clock() - start_time))

novo_usuario = cadastrar_usuario()
os.system('clear')

d = novo_usuario['data_cadastro']

print(d.strftime("%d de %B de %Y, %H:%M"))  #como mudar para o português?
