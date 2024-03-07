start = int(input('Unesite donju granicu: '))
end = int(input('Unesite gornju granicu: '))

suma = 0

for i in range(start, end+1):
    if i % 3 == 0 and i % 6 != 0:
        suma += pow(i, 2)
print(suma)
