import random

print('='*40)
print('''Program looping (while dan for)
Tentang menampilkan n bilangan acak
yang lebih kecil dari 0.5''')
print('='*40)

n = int(input("Masukan jumlah n: "))
for i in range(n):
    a = random.uniform(0.0, 0.5)
    print(a)
