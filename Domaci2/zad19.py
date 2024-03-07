skolarina = eval(input('Unesite iznos skolarine: '))
prosjek = eval(input('Unesite prosjecnu ocjenu ucenika: '))
nagrade = int(input('Unesite \'1\' ukoliko ucenik ima nagradu, u suprotnom unesite \'0\': '))
popust = 0
if 4.5 <= prosjek <= 5.0:
    popust += 0.4
elif 3.5 <= prosjek <= 4.5:
    popust += 0.2
elif 2.5 <= prosjek <= 3.5:
    popust += 0.1

if nagrade == 1:
    popust += 0.3
skolarina = skolarina * (1-popust)

print(f'Popust na skolarinu prilikom upisa u narednu godinu je {skolarina}')
