lista = input('Unesite karaktere: ').split()
for i in range(len(lista)):
    lista[i] = eval(lista[i])
suma = 0
for i in lista:
    if i % 3 == 0:
        suma += pow(i, 2)
print(suma)
