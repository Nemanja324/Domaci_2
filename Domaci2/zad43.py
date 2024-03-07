ocjene = input('Unesite zeljeni niz: ').split()
petice = 0
cetvorke = 0
trojke = 0
for i in range(len(ocjene)):
    ocjene[i] = eval(ocjene[i])
for i in range(len(ocjene)):
    if ocjene[i] == 5:
        petice += 1
    elif ocjene[i] == 4:
        cetvorke += 1
    elif ocjene[i] == 3:
        trojke += 1
    else:
        pass
print(f'Petica je: {petice}')
print(f'Cetvorki je: {cetvorke}')
print(f'Trojki je: {trojke}')
