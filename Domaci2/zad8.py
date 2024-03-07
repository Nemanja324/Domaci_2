ocjene = input('Unesite ocjene ucenika: ').split()

for i in range(len(ocjene)):
    ocjene[i] = eval(ocjene[i])

if 1 not in ocjene:
    uspjeh = sum(ocjene)/len(ocjene)
    if uspjeh >= 4.5:
        print('Odlican')
    elif uspjeh >= 3.5:
        print('Vrlodobar')
    elif uspjeh >= 2.5:
        print('Dobar')
    elif uspjeh >= 2:
        print('Dovoljan')
else:
    print('Nedovoljan')
