tekst = input('Unesite tekst: ')
broj = ''
for i in range(len(tekst)):
    if tekst[i] < '0' or tekst[i] > '9':
        broj += tekst[i]
print(broj)
