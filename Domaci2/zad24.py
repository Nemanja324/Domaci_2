tekst = input('Unesi tekst:')

if len(tekst) > 30:
    novi_tekst = tekst[:30]
    novi_tekst += '...'
    print(novi_tekst)
