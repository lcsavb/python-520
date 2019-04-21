lista_de_gatos = [
    {
        'nome': 'Malawi',
        'peso': 3750,
        'idade': 3,
        'apelido': 'Oncinha'
    },
    {
        'nome': 'Gato',
        'peso': 6000,
        'idade': 6,
        'apelido': 'Sedoso'
    }
]


def get_input_as_int(mensagem, erro):
    user_input = input(mensagem)
    try:
        return int(user_input)
    except ValueError:
        raise ValueError(erro)


def tratamento_de_tentativas(numero_tentativas, mensagem, erro):
    for tentativa in range(numero_tentativas):
        try:
            return get_input_as_int(mensagem, erro)
        except ValueError as err:  # não entendi essa parte
            restantes = numero_tentativas - (tentativa + 1)
            print('Um erro aconteceu')
            print(err)
    print('Você errou o input {} vezes.'.format(numero_tentativas))
    print('Vou encerrar o programa, pois você é burro demais!')


novo_gato = {
    'nome': input('Digite o nome do gato:\n'),
    'peso': tratamento_de_tentativas(
        5, 'Digite o peso: \n', 'O peso deve ser um número maior que 0!'),
    'idade': tratamento_de_tentativas(
        5, 'Digite a idade: \n', 'A idade deve ser um número maior que 0!'),
    'apelido': input('Digite o apelido do gato:\n')
}

lista_de_gatos.append(novo_gato)

for gato in lista_de_gatos:
    if gato['peso'] > 5000:
        print('Esse é o Gato')
else:
    print('Ela é a Malawi')
