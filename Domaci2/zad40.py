niz_brojeva = input('Unesite zeljeni niz: ').split()
for i in range(len(niz_brojeva)):
    niz_brojeva[i] = int(niz_brojeva[i])
suma = 0
for i in range(len(niz_brojeva)):
    if niz_brojeva[i] < 0 and niz_brojeva[i] % 2 == 0:
        suma += abs(niz_brojeva[i])
print(suma)
