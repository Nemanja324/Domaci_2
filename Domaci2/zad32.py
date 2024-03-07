a = int(input('Unesite donju granicu: '))
b = int(input('Unesite gornju granicu: '))
djelilac = int(input('Unesite djelioca: '))
suma = 0
brojac = 0
for i in range(a+1, b):
    if i % djelilac == 0:
        suma += i
        brojac += 1
print(f'Suma je: {suma}, broj clanova je {brojac}')
