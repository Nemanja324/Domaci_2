n = input('Unesite cetvorocifreni broj: ')

if len(n) == 4:
    n = int(n)
    if n % 2 == 0:
        zbir = 0
        while n > 0:
            if (n % 10) % 2 == 0:
                zbir += n % 10
            n = n // 10
        print(f'Posto je broj paran suma parnih cifara je {zbir}')
    else:
        proizvod = 1
        while n > 0:
            if (n % 10) % 2 != 0:
                proizvod *= n % 10
            n = n // 10
        print(f'Posto je broj neparan proizvod neparnih cifara je {proizvod}')
else:
    print('Nisi unijo cetvorocifreni broj bajo.')
