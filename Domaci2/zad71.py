from math import sqrt
from math import floor
brojevi = input('Unesite listu brojeva: ').split()
brojac = 0
for j in range(len(brojevi)):
    brojevi[j] = eval(brojevi[j])

for i in brojevi:
    if sqrt(i) == floor(sqrt(i)):
        brojac += 1
print(brojac)
