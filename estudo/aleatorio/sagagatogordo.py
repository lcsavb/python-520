lista_de_gatos = [
    {
        'nome': 'Malawi',
        'idade': 3,
        'peso': 3750
    },
    {
        'nome': 'Gato',
        'idade': 6,
        'peso': 6000
    }
]

gatos_gordos = []
gatos_magros = []


def cadastrar_gatos():
    gato = {
        'nome': input('Digite o nome do gato: \n'),

        'idade': conserto_erros_do_cadastro(
            'Digite a idade do gato: \n', 'Idade cadastrada com sucesso!', 'Idade inválida, tente novamente!)'),
        'peso': conserto_erros_do_cadastro(
            'Digite o peso do gato: \n', 'Peso cadastrado com sucesso!', 'Peso inválido, tente novamente!)')
    }
    return gato


def conserto_erros_do_cadastro(mensagem_para_cadastro, mensagem_de_sucesso, mensagem_de_erro):
    while True:
        try:
            entrada_do_usuario_bozo = checar_se_inteiro(mensagem_para_cadastro)
            print(mensagem_de_sucesso)
            break
        except ValueError:
            print(mensagem_de_erro)
    return entrada_do_usuario_bozo


def checar_se_inteiro(mensagem_para_cadastro):
    try:
        entrada_usuario = int(input(mensagem_para_cadastro))
    except ValueError:
        raise
    return entrada_usuario


for gato in range(3):
    lista_de_gatos.append(cadastrar_gatos())


TEMPLATE = '{:>16} ||| {:>16} ||| {:>16}'


CABECALHO = TEMPLATE.format('Nome do gatinho', 'Idade', 'Peso')


print(CABECALHO)
for gato in lista_de_gatos:
    gato_ajustado = TEMPLATE.format(
        gato['nome'],
        gato['idade'],
        gato['peso']
    )
    print(gato_ajustado)


for gato in lista_de_gatos:
    if gato['peso'] > 5000:
        gatos_gordos.append(gato)
    else:
        gatos_magros.append(gato)


print('Esses são os gatos magros:')
print(gatos_magros)


print('Esses são os gatos gordos:')
print(gatos_gordos)

