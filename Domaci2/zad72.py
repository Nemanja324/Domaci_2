ocjene = input('Unesite listu brojeva: ').split()
prosjek = 0
for j in range(len(ocjene)):
    ocjene[j] = eval(ocjene[j])

for i in range(len(ocjene)):
    if ocjene[i] != 5:
        prosjek += ocjene[i]
prosjek = prosjek/(len(ocjene)-ocjene.count(5))
print(round(prosjek, 3))
