temperatura = int(input('Unesite temperaturu vode: '))

if 0 < temperatura < 100:
    print('tecno')
elif temperatura >= 100:
    print('gasovito')
elif temperatura <= 0:
    print('cvrsto')
