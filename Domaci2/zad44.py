utakmice = input('Unesite zeljeni niz: ').split()
for i in range(len(utakmice)):
    utakmice[i] = eval(utakmice[i])
print(max(utakmice))
