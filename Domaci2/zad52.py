tekst = input('Unesite zeljeni tekst: ')
pre = input('Unesite prefiks: ')
suf = input('Unesite sufinks: ')
num = int(input('Unesite koliko puta zelite da se prefiks i sufiks ponavljaju: '))

pre *= num
suf *= num
print(pre+tekst+suf)
