tekst = input('Unesite tekst: ')
broj = ''
for i in range(len(tekst)):
    if '0' <= tekst[i] <= '9':
        broj += tekst[i]
print(f'Broj je : {int(broj)}')
