plate = input('Unesite zeljeni niz: ').split()
for i in range(len(plate)):
    plate[i] = eval(plate[i])
prosjek = sum(plate) / len(plate)
brojac = 0
for i in plate:
    if i > prosjek:
        brojac += 1
print(brojac)
