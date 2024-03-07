sati = float(input('Unesite koliko je sati: '))

if sati > 23 or sati < 1:
    print('Unijeli ste izmisljenje sate.')
elif sati <= 6 or sati >= 22:
    print('Ne smijete da radite')
elif 13 <= sati <= 17:
    print('Ne smijete da radite')
else:
    print('Smijete da radite')
