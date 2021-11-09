print('='*40)
print('''\tModul Praktikum 2
\tSTRUKTUR KONDISI
\nProgram Menampilkan Bilangan Terbesar
dari 3 Buah Bilangan Inputan
''')
print('='*40)

x = int(input('Masukan bilangan pertama : '))
y = int(input('Masukan bilangan kedua : '))
z = int(input('Masukan bilangan ketiga : '))

if x > y:
    if x > z:
        print('\nBilangan Terbesar = ', x)
elif y > z:
    print('\nBilangan terbesar = ', y)
else:
    print('\nBilangan terbesar = ', z)
print('='*40)
