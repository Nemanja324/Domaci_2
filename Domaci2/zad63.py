tekst = input('Unesite tekst: ').split()
najduza = ''
for i in tekst:
    if len(i) > len(najduza):
        najduza = i
print(najduza)
