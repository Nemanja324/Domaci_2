prvi_proizvod = float(input('Unesite cijenu prvog proizvoda: '))
drugi_proizvod = float(input('Unesite cijenu drugog proizvoda: '))
treci_proizvod = float(input('Unesite cijenu treceg proizvoda: '))

if prvi_proizvod > drugi_proizvod and prvi_proizvod > treci_proizvod:
    print(f'Drugi i treci sa cijenom od {drugi_proizvod + treci_proizvod}')
elif drugi_proizvod > prvi_proizvod and drugi_proizvod > treci_proizvod:
    print(f'Prvi i treci sa cijenom od {prvi_proizvod + treci_proizvod}')
else:
    print(f'Prvi i drugi sa cijenom od {prvi_proizvod + drugi_proizvod}')
