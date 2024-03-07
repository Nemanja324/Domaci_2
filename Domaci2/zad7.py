moja_lista = []
broj_studenata = int(input('Koliko ima studenata: '))
for i in range(broj_studenata):
    pom = {}
    moj_objekat = {}
    ime = input('Unesite ime studenta: ')
    matem = int(input(f'Broj bodova iz matem: '))
    prog = int(input(f'Broj bodova iz prog: '))
    pom['Matematika'] = matem
    pom['Programiranje'] = prog
    moj_objekat['Ime'] = ime
    moj_objekat['Bodovi'] = pom
    moja_lista.append(moj_objekat)
prog = 0
bodovi = 0
ime = ''
for i in range(broj_studenata):
    if moja_lista[i]['Bodovi']['Matematika'] + moja_lista[i]['Bodovi']['Programiranje'] > bodovi:
        ime = moja_lista[i]['Ime']
        bodovi = moja_lista[i]['Bodovi']['Matematika'] + moja_lista[i]['Bodovi']['Programiranje']
        prog = moja_lista[i]['Bodovi']['Programiranje']
    elif moja_lista[i]['Bodovi']['Matematika'] + moja_lista[i]['Bodovi']['Programiranje'] == bodovi:
        if moja_lista[i]['Bodovi']['Programiranje'] > prog:
            ime = moja_lista[i]['Ime']
        bodovi = moja_lista[i]['Bodovi']['Matematika'] + moja_lista[i]['Bodovi']['Programiranje']
        prog = moja_lista[i]['Bodovi']['Programiranje']
print(f'Pobjednik takmicenja je {ime}!!!')
