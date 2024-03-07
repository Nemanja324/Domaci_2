broj = eval(input('Unesite dvocifreni broj: '))
druga_cif = broj % 10
prva_cif = broj // 10
if prva_cif > druga_cif:
    print(f'Razlika je: {prva_cif-druga_cif}')
elif prva_cif < druga_cif:
    print(f'Zbir je: {prva_cif + druga_cif}')
else:
    print(f'Proizvod je: {prva_cif * druga_cif}')
