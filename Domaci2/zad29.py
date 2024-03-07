broj = input('Unesi broj:')

ind = True
for i in range(len(broj)):
    if broj[i] != '0' and broj[i] != '1':
        ind = False
        break
if ind:
    print('Broj je binarni.')
else:
    print('Broj nije binarni.')
