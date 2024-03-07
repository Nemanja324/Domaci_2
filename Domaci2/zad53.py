import random
broj_golova = int(input('Unesi broj golova: '))
lista = ['a', 'b']
a = 0
b = 0
suma = 0
while suma != broj_golova:
    if random.choice(lista) == 'a':
        a += 1
    else:
        b += 1
    suma += a + b
print(a)
print(b)
print(a+b)
