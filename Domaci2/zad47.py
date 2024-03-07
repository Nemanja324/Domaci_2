tri_broja = input('Unesite 3 broja: ').split()
for i in range(len(tri_broja)):
    tri_broja[i] = eval(tri_broja[i])
print('Najveci:', max(tri_broja))
print('Najmanji:', min(tri_broja))
