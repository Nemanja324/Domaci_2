radovi = int(input('Unesite \'1\' ako je student predao sve seminarske radove, u suprotnom unesite \'0\': '))
prisustvo = int(input('Unesite prisustvo studenta: '))

if prisustvo >= 75 and radovi:
    print('Student moze da pristupi ispitu')
else:
    print('Student ne moze da pristupi ispitu')
