
#retornar apenas os pares

def par(x):
    if x % 2 == 0:
        return True
    return False

def incrementar(x):
    return x + 1

def gerar_lista_numeros_pares(numero):
    return [incrementar(i + 1) for i in range(numero) if par(i)]

lista_numeros_pares = gerar_lista_numeros_pares(5)

for numero in lista_numeros_pares:
    if not par(numero):
        raise Exception('{} não é um número par'.format(numero))

# # exit()

# # escrever uma função que recebe
# # um número inteiro e retorna uma lista com todos os números
# # menores ou iguais a esse com exceção do zero
# # a forma que eu fiz

# def gerar_lista(x):
#     lista = []
#     for n in range(x):
#         if n != 0:
#             lista.append(n)
#     lista.append(x)
#     return lista

# print(gerar_lista(10))


# # forma 1
# def gerar_lista1(numero):
#     lista,x = [], 1
#     while x <= numero:
#         lista.append(x)
#         x += 1
#     return lista

# # forma 2
# def gerar_lista2(numero):
#     lista = []
#     for i in range(numero):
#         lista.append(i + 1)
#     return lista

# # forma 3
# def gerar_lista3(numero):
#     return [i + 1 for i in range(numero)]

# # forma 4
# gerar_lista = lambda n: [i + 1 for i in range(n)]
# print(gerar_lista(5))