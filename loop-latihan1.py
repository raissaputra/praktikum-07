import random

print('='*40)
print('''\tModul Praktikum 3
\tPERULANGAN
\nProgram looping (while dan for)
Tentang menampilkan n bilangan acak
yang lebih kecil dari 0.5
''')
print('='*40)

n = int(input("Masukan nilai N : "))
for i in range(n):
    a = random.uniform(0.0, 0.5)
    print("Data ke :", i+1, "=> ", a)
print('Selesai')
