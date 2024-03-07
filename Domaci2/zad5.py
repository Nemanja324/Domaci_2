a = float(input('Unesite duzinu prve strane: '))
b = float(input('Unesite duzinu druge strane: '))
c = float(input('Unesite duzinu trece strane: '))

if a + b > c and b + c > a and c + a > b:
    print('Moze da se napravi')
else:
    print('Ne moze da se napravi')
