tekst = input('Unesite zeljeni tekst: ')
pozicija = int(input('Unesite zeljenu poziciju: '))

if pozicija == 0:
    if tekst[pozicija+1] == '0':
        print('1')
    else:
        print('0')
elif pozicija == len(tekst)-1:
    if tekst[pozicija-1] == '0':
        print('1')
    else:
        print('0')
else:
    br = 0
    if tekst[pozicija-1] == '0':
        br += 1
    if tekst[pozicija+1] == '0':
        br += 1
    print(br)
