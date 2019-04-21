import datetime


data = datetime.datetime.now()

ano_atual = data.strftime('%Y')

nome = input('Digite o seu nome: ')

idade = input('Digite a sua idade: ')

ano_nascimento = int(ano_atual) - int(idade)

mensagem = '{}, você terá 100 anos de idade em: '.format(nome)

print(mensagem)
print(ano_nascimento + 100)

numero = input('Digite um novo número: ')

print(mensagem * int(numero))
