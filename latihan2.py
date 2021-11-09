print('='*40)
print('''\tModul Praktikum 2
\tSTRUKTUR KONDISI
\nProgram Mengurutkan 3 data inputan
dan tampilkan hasilnya secara berururtan
dari data terkecil ke data terbesar
''')
print('='*40)

print('Program mengurutkan data :')
a = int(input('Bilangan ke-1 = '))
b = int(input('Bilangan ke-2 = '))
c = int(input('Bilangan ke-3 = '))

if a < b:
    if b < c:
        print('Urutan bilangan : ', a, b, c)
    else:
        if a < c:
            print('Urutan bilangan : ', a, c, b)
        else:
            print('Urutan bilangan : ', c, a, b)
else:
    if a < c:
        print('Urutan bilangan : ', b, a, c)
    else:
        if b < c:
            print('Urutan bilangan : ', b, c, a)
        else:
            print('Urutan bilangan : ', c, b, a)
print('='*40)
