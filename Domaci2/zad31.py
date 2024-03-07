start = int(input('Unesite donju granicu: '))
end = int(input('Unesite gornju granicu: '))

suma = 0

for i in range(start, end+1):
    if i % 2 == 0 and i % 4 != 0:
        suma += pow(i, 2)
print(suma)
