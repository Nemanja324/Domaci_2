godina = int(input('Unesite godinu: '))

if godina % 4 == 0:
    if godina % 100 == 0:
        if godina % 400 == 0:
            print(f'Godina {godina} je prestupna.')
        else:
            print(f'Godina {godina} nije prestupna.')
    else:
        print(f'Godina {godina} je prestupna.')
else:
    print(f'Godina {godina} nije prestupna.')
