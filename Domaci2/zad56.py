tekst = input('Unesite string: ')

brojac = 0
i = 0

while i < len(tekst):
    if tekst[i] == '-':
        if i + 2 < len(tekst):
            if tekst[i+2] == '+' or tekst[i+2] == '-':
                brojac += 1
            else:
                pass
        else:
            brojac += 1
    else:
        pass
    i += 1
print(brojac)
