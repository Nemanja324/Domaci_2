niz_brojeva = input('Unesite zeljeni niz: ').split()
broj = int(input('Unesite broj: '))
for i in range(len(niz_brojeva)):
    niz_brojeva[i] = eval(niz_brojeva[i])
br_elemenata = 0
for i in range(len(niz_brojeva)):
    if niz_brojeva[i] < broj:
        br_elemenata += 1
print(f'Broj elemenata manjih od broja je {br_elemenata}')
