def funkcija(num):
    global najmanji
    global najveci
    if len(num) > 1:
        num = eval(num)
        while num > 0:
            if najveci < num % 10:
                najveci = num % 10
            elif najmanji > num % 10:
                najmanji = num % 10
            else:
                pass
            num //= 10
    else:
        najmanji = najveci = eval(num)


broj = input('Unesite broj: ')
najmanji = 999
najveci = 0
funkcija(broj)  # Nalazi najmanju i najvecu cifru broja
print('Najmanja:', najmanji)
print('Najveca:', najveci)
