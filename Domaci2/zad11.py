mrav = input('Unesite kordinate mrava: ').split()
sto_gore_desno = input('Unesite kordinate gornje desne ivice stola: ').split()
sto_dolje_lijevo = input('Unesite kordinate donje lijeve ivice stola: ').split()
for i in range(len(mrav)):
    mrav[i] = eval(mrav[i])
    sto_dolje_lijevo[i] = eval(sto_dolje_lijevo[i])
    sto_gore_desno[i] = eval(sto_gore_desno[i])
if mrav[0] >= 0:
    if mrav[0] == sto_gore_desno[0] and -(sto_gore_desno[1]) <= mrav[1] <= sto_gore_desno[1]:
        print('Krece se po ivici')
    elif mrav[1] == sto_gore_desno[1] and -(sto_gore_desno[0]) <= mrav[0] <= sto_gore_desno[0]:
        print('Krece se po ivici')
    else:
        print('Ne krece se po ivici')
else:
    if mrav[0] == sto_dolje_lijevo[0] and sto_dolje_lijevo[1] <= mrav[1] <= abs(sto_dolje_lijevo[1]):
        print('Krece se po ivici')
    elif mrav[1] == sto_dolje_lijevo[1] and sto_dolje_lijevo[0] <= mrav[0] <= abs(sto_dolje_lijevo[0]):
        print('Krece se po ivici')
    else:
        print('Ne krece se po ivici')
