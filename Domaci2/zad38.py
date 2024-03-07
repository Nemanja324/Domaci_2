broj = input('Unesite broj: ')
novi_broj = ''
for i in range(len(broj)):
    if int(broj[i]) % 2 == 0:
        novi_broj += '0'
    else:
        novi_broj += '1'
print(novi_broj)
