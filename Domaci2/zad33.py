broj = int(input('Unesi broj:'))
suma = 0
while broj > 0:
    suma += broj % 10
    broj //= 10
print(suma)
