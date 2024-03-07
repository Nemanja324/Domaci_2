proizvodi = input('Unesite zeljeni niz: ').split()
popust = eval(input('Unesite popust: '))
for i in range(len(proizvodi)):
    proizvodi[i] = eval(proizvodi[i])
stara_cijena = sum(proizvodi)
for i in range(len(proizvodi)):
    proizvodi[i] = proizvodi[i] * (1-(popust/100))
nova_cijena = sum(proizvodi)

print(f'Razlika stare i nove cijene je: {round(stara_cijena - nova_cijena, 2)}')
