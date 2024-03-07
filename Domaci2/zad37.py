tekst = input('Unesite tiket: ')
poeni = 0
for i in range(len(tekst)):
    if tekst[i] == '1':
        poeni += 1
    elif tekst[i] == '0':
        poeni += 0
    elif tekst[i] == '*':
        poeni -= 1
print(poeni)
