tekst = input('Unesi tekst:')
proizvod = 1
for i in range(len(tekst)):
    if tekst[i] >= '0' and tekst[i] <= '9':
        proizvod *= int(tekst[i])
print(f'Proizvod je: {proizvod}')
