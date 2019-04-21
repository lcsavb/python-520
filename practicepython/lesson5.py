# Achar a intersecção entre duas listas, sem valores repetidos.

import random

#
# a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
# b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
#
#
# print(a & b)

#Gerar duas listas randômicas para testar a solução encontrada.

lista1 = []
lista2 = []

for n in range(300):
    lista1.append(n)
    lista2.append(n)

random.shuffle(lista1)
random.shuffle(lista2)

print(lista1)
print(lista2)

a = set(lista1[0:150])
b = set(lista2[0:150])
c = a & b

print(a)
print(b)
print(c)


