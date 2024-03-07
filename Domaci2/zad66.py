lista = input('Unesite brojeve: ').split()
dvocifreni = 0
trocifreni = 0
for i in lista:
    if len(i) == 3:
        trocifreni += 1
    elif len(i) == 2:
        dvocifreni += 1
    else:
        pass
if dvocifreni > trocifreni:
    print('Dvocifrenih ima vise.')
elif dvocifreni < trocifreni:
    print('Trocifrenih ima vise.')
else:
    print('Ima ih jednako.')
