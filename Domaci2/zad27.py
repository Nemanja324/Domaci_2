tekst = input('Unesi tekst:')
if 'a' not in tekst:
    if 'e' not in tekst:
        if 'i' not in tekst:
            if 'o' not in tekst:
                if 'u' not in tekst:
                    print('Nema samoglasnika.')
                else:
                    print('Ima samoglasnika.')
            else:
                print('Ima samoglasnika.')

        else:
            print('Ima samoglasnika.')
    else:
        print('Ima samoglasnika.')
else:
    print('Ima samoglasnika.')
