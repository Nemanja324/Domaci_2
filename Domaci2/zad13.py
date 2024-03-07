from math import pi
r1 = eval(input('Unesi poluprecnik prvog stola: '))
r2 = eval(input('Unesi poluprecnik drugog stola: '))

if r1*r1*pi > r2*r2*pi:
    print('Prvi sto ima vecu povrsinu.')
elif r1 * r1 * pi < r2 * r2 * pi:
    print('Drugi sto ima vecu povrsinu.')
else:
    print('Oba stola imaju istu povrsinu.')
