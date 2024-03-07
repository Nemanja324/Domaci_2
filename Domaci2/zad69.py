zarade = input('Unesite zarade: ').split()
for i in range(len(zarade)):
    zarade[i] = eval(zarade[i])
brojac = 0
prosjek = sum(zarade)/len(zarade)

for i in zarade:
    if i > prosjek:
        i = i * 0.9
    else:
        i = i * 1.1
    if i > prosjek:
        brojac += 1
print(brojac)
