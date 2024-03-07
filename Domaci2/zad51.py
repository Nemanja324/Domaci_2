tekst = input('Unesite loznku: ')
ind_velika = 0
ind_mala = 0
ind_cif = 0

for i in tekst:
    if 'a' <= i <= 'z':
        ind_mala += 1
    elif 'A' <= i <= 'Z':
        ind_velika += 1
    elif '0' <= i <= '9':
        ind_cif += 1
if ind_velika > 0 and ind_mala > 0 and ind_cif > 0:
    print('Yes')
else:
    print('No')
