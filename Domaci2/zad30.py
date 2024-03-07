broj = int(input('Unesi broj:'))
par = 0
nepar = 0
suma = 0
proizvod = 1
for i in range(1, broj+1):
    if i % 2 == 0:
        par += 1
        suma += i
    else:
        nepar += 1
        proizvod *= i
print(f'Zbir je: {suma}, a proizvod je {proizvod}')
print(f'Parnih brojeva je: {par}, neparnih brojeva je: {nepar}')
