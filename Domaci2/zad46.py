plate = input('Unesite zeljeni niz: ').split()
for i in range(len(plate)):
    plate[i] = eval(plate[i])
najveca = max(plate)
druga_najveca = 9999
for i in plate:
    if najveca - i < druga_najveca and najveca != i:
        druga_najveca = i
print(druga_najveca)
