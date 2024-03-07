def funkcija(num, stepen):

    '''Nalazi sumu cifara broja, a cifre su stepenovane brojem cifara broja. '''

    suma = 0
    while num > 0:
        suma += pow(num % 10, stepen)
        num //= 10
    return suma


broj = input('Unesite broj: ')
duzina = len(broj)
broj = int(broj)
if funkcija(broj, duzina) == int(broj):
    print('Da')
else:
    print('Ne')
