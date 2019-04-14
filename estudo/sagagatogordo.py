import datetime

lista_de_gatos = [
    {
        'nome': 'Malawi',
        'peso': 3750
    },
    {
        'nome': 'Gato',
        'peso': 6000
    }
]

gatos_gordos = []
gatos_magros = []


def cadastrar_gatos():
    gato = {
        'nome': input('Digite o nome: \n'),

        'idade': conserto_erros_do_cadastro(
            'Digite a idade do gato: ', 'Idade cadastrada com sucesso!', 'Idade inválida, tente novamente)'),
        'peso': conserto_erros_do_cadastro(
            'Digite o peso do gato: ', 'Peso cadastrado com sucesso!', 'Peso inválido, tente novamente)')
    }
    return gato


# def change_to_int(mensagem_para_cadastro, mensagem_de_erro):
# 	entrada_usuario = input(mensagem_para_cadastro)
# 	try:
# 		return int(entrada_usuario)
# 	except ValueError:
# 		raise ValueError(mensagem_de_erro)


def conserto_erros_do_cadastro(mensagem_para_cadastro, mensagem_de_sucesso, mensagem_de_erro):
    while not False:
        try:
            entrada_do_usuario_bozo = int(input(mensagem_para_cadastro))
            print(mensagem_de_sucesso)
            break
        except ValueError:
            print(mensagem_de_erro)
    return entrada_do_usuario_bozo


for gato in range(1):
    lista_de_gatos.append(cadastrar_gatos())

print(lista_de_gatos)

for gato in lista_de_gatos:
    if gato['peso'] > 5000:
        gatos_gordos.append(gato)
else:
    gatos_magros.append(gato)


print('Esses são os gatos magros:')
print(gatos_magros)


print('Esses são os gatos gordos:')
print(gatos_gordos)
