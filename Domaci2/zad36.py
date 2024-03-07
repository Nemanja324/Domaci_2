tekst = input('Unesite tekst: ').lower()
izlaz = ''
for i in range(len(tekst)):
    if tekst[i] == 'a' or tekst[i] == 'e' or tekst[i] == 'i' or tekst[i] == 'o' or tekst[i] == 'u':
        izlaz += '1'
    else:
        izlaz += '0'
print(izlaz)
