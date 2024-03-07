tekst = input('Unesite string proizvoljne duzine: ')
duzina = int(input('Unesite duzinu: '))
novi_tekst = ''
if len(tekst) <= duzina:
    novi_tekst += (tekst + '...')
else:
    for i in range(duzina):
        novi_tekst += tekst[i]
    novi_tekst += '...'
print(novi_tekst)
