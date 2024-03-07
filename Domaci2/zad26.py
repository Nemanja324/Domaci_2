broj = input('Unesi broj:')
if broj.count('0b') > 0:
    print(f'Broj {broj} je binarni broj')
elif broj.count('0o') > 0:
    print(f'Broj {broj} je oktalni broj')
elif broj.count('0x') > 0:
    print(f'Broj {broj} je heksadecimalni broj')
else:
    print(f'Broj {broj} je dekadni broj')
