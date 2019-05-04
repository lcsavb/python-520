# capitais = {"United States": "Washington",
#             "Canada": "Ottawa",
#             "Germany": "Berlin",
#             "France": "Paris",
#             "England": "London",
#             "UK": "London",
#             "Switzerland": "Bern",
#             "Austria": "Vienna",
#             "Netherlands": "Amsterdam",
#             "Brazil": "Brasília"
#             }
#
#
# TEMPLATE = "{:>15}||{:>15}"
#
#
# separador = '>>>>>'
#
# print(TEMPLATE.format('Countries', 'Capitals'))
# for country in capitais:
#     print(TEMPLATE.format(country, capitais[country]))


# Exercício: o usuário digita o seu continente, o output é uma lista dos países e após a segunda escolha,
# mostrar qual é a capital do respectivo país.


america_sul = {
    'Brasil': 'Brasília',
    'Paraguai': 'Assunção',
    'Chile': 'Santiago'
}

america_norte = {
    'EUA': 'Washington',
    'México': 'Cidade do México',
    'Canada': 'Toronto'
}

europa = {
    'Reino Unido': 'Londres',
    'Espanha': 'Madri',
    'República Checa': 'Praga'
}

asia = {
    'Japão': 'Tokio',
    'China': 'Pequim',
    'Tailândia': 'Bangcok'
}

africa = {
    'Egito': 'Cairo',
    'Marrocos': 'Marrakesh',
    'Angola': 'Luanda'
}


continente_usuario = input('Digite o seu continente > ')


def selecionar_continente():
    if continente_usuario.lower() == 'africa':
        for paises in africa:
            print(paises)
    elif continente_usuario.lower() == 'asia':
        for paises in asia:
            print(paises)
    elif continente_usuario.lower() == 'europa':
        for paises in europa:
            print(paises)
    elif continente_usuario.lower() == 'américa do sul':
        america_sul = chave
        for paises in america_sul:
            print(paises)


def selecionar_pais(continente_usuario):
    print('Escolha o país no' + continente_usuario + ': ')
    selecionar_continente()
    pais_usuario = input('Digite o país no qual está localizado: ')
    print(chave[pais_usuario])


selecionar_pais()




