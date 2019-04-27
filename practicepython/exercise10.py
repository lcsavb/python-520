import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [x for x in set(a) for y in set(b) if x == y]

print(c)

d = [element for element in range(100)]

e = random.choices(d,k=random.randint(0,20))
f = random.choices(d,k=random.randint(0,20))

print(e)
print(f)

h = [n for n in set(e) for y in set(f) if n == y]

print(h)