variavel = 11

resultado_bool = variavel < 10

if resultado_bool:
    print(True)
else:
    print(False)

lista_de_numeros = [1, 2, 3, 4, 5]
for numero in lista_de_numeros:
    if numero % 2 == 0:
        print('Par')
    else:
        print(numero)

try:
    idade = int(input('Digite a sua idade: '))
    print('Sua idade é: {}'.format(idade))
except:
    print('Idade Inválida')
finally: #não é boa prática
    print('Sempre será executado')

exit()

for letra in 'Lucas Amorim Vieira de Barros':
    if letra == 'a' or letra == 'm':
        print(letra)
    else:
        print('Deu ruim')

