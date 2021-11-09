# praktikum-07
## Tugas 05  di pertemuan ke-07 (Bahasa Pemrograman)

### Program Menampilkan Bilangan Terbesar dari 3 Buah Bilangan Inputan
* FLOWCHART :
* ![img](https://github.com/raissaputra/praktikum-07/blob/main/screenshot/tiga.jpg)
* OUTPUT PROGRAM tugas-praktikum2.py:
* ![img](https://github.com/raissaputra/praktikum-07/blob/main/screenshot/bil-terbesar.png)
* PENJELASAN :
  * untuk inisialisasi nilai yang diinput dari user dan menyimpannya di variabel x,y,z :
  * ```
    x = int(input('Masukan bilangan pertama : '))
    y = int(input('Masukan bilangan kedua : '))
    z = int(input('Masukan bilangan ketiga : '))
    ```
  * mengecek kondisi 3 nilai yang diinputkan dan mencetak bilangan terbesar nya :
  * ```
    if x > y:
        if x > z:
            print('\nBilangan Terbesar = ', x)
        elif y > z:
            print('\nBilangan terbesar = ', y)
        else:
            print('\nBilangan terbesar = ', z)
    ```

### Program Menampilkan Bilangan Terbesar dari 2 Buah Bilangan Inputan dengan statement if
* FLOWCHART :
* ![img](https://github.com/raissaputra/praktikum-07/blob/main/screenshot/dua.jpg)
* OUTPUT PROGRAM latihan1.py :
* ![img](https://github.com/raissaputra/praktikum-07/blob/main/screenshot/2bilbesar.png)
* PENJELASAN :
  * untuk inisialisasi nilai yang diinput dari user dan menyimpannya di variabel x,y :
  * ```
    x = int(input('Masukan bilangan pertama : '))
    y = int(input('Masukan bilangan kedua : '))
    ```
  * mengecek kondisi 2 nilai yang diinputkan dan mencetak bilangan terbesar nya :
  * ```
    if x > y:
        print('\nBilangan terbesar = ', x)
    else:
        print('\nBilangan terbesar = ', y)
    ```

### Program Mengurutkan 3 data inputan dan tampilkan hasilnya secara berururtan dari data terkecil ke data terbesar
* FLOWCHART :
* ![img](https://github.com/raissaputra/praktikum-07/blob/main/screenshot/satu.jpg)
* OUTPUT PROGRAM latihan2.py :
* ![img](https://github.com/raissaputra/praktikum-07/blob/main/screenshot/urut-data.png)
* PENJELASAN :
  * untuk inisialisasi nilai yang diinput dari user dan menyimpannya di variabel a, b, c 
  * ```
    a = int(input('Bilangan ke-1 = '))
    b = int(input('Bilangan ke-2 = '))
    c = int(input('Bilangan ke-3 = '))
    ```
  * mengecek kondisi nilai yang diinputkan dan mencetaknya dengan urutan dari bilangan terkecil s/d terbesar
  * ```
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
    ```

### Program Sederhana dengan Perulangan Tentang Keuntungan perbulan seorang Pengusaha
* OUTPUT PROGRAM program1.py :
* ![img](https://github.com/raissaputra/praktikum-07/blob/main/screenshot/laba.png)
* PENJELASAN :
  * tetapkan dulu nilai dan simpan pada variabel :
  * ```
    n = 100000000
    sum = 0
    y = 0
    ```
  * buat rumus presentase keuntungan tiap bulannya sesuai soal & simpan di variabel laba :
  * ```
    laba = [int(0), int(0), int(n) * 0.01, int(n) * 0.01, int(n) *
        0.05, int(n) * 0.05, int(n) * 0.05, int(n) * 0.02]
    ```
  * lakukan perulangan pada variabel laba dan mencetak hasilnya sesuai index yang sudah dibuat :
  * ```
    for i in laba:
        sum = sum+i
        y += 1
        print('Laba bulan ke-', y, 'sebesar : ', i)
    ```
  * jumlahkan semua total laba(sum) dan mencetaknya :
  * ```
    print('Total laba adalah : ', sum)

    ```
### Program looping (while dan for) Tentang menampilkan n bilangan acak yang lebih kecil dari 0.5
* OUTPUT PROGRAM loop-latihan1.py :
* ![img](https://github.com/raissaputra/praktikum-07/blob/main/screenshot/random.png)
* PENJELASAN :
  * input dan simpan nilai dari user : 
  * ```
    n = int(input("Masukan nilai N : "))
    ```
  * lakukan perulangan dan variabel n sebagai batasan looping nya
  * jangan lupa **import random** untuk membangkitkan nilai random
  * variabel a untuk menyimpan batasan nilai <0.5
  * dan cetak nilai a dengan i sebagai index nya
  * ```
    for i in range(n):
        a = random.uniform(0.0, 0.5)
        print("Data ke :", i+1, "=> ", a)
    ```
  
### Program Dengan Perulangan Bertingkat (nested) for
* OUTPUT PROGRAM lab2.py :
* ![img](https://github.com/raissaputra/praktikum-07/blob/main/screenshot/looping.png)
* PENJELASAN :
  * untuk mencetak hasil looping sesuai modul materi, berikut codingan nya :
  * ```
    for i in range(0, 10):
        for j in range(0, 10):
            product = i+j
            print(f"{product:>3}", end='')
        print()
    ```
  * PENJELASAN SINGKAT :
    * untuk menentukan batasan nilai yang akan di looping dengan range(0, 10)
    * ada 2 nama variabel yaitu i dan j, untuk menyimpan hasil loop nya
    * variabel product untuk menyimpan nilai dari hasil variabel i dan j
    * untuk spasi antar nilai dengan **print(f"{product:>3}", end='')**
    * untuk baris baru dengan **print()**
  
### Program looping (while dan for) Tentang menampilkan n bilangan acak yang lebih kecil dari 0.5
* OUTPUT PROGRAM lab1.py :
* ![img](https://github.com/raissaputra/praktikum-07/blob/main/screenshot/random2.png)
* PENJELASAN :
  * input dan simpan nilai dari user : 
  * ```
    n = int(input("Masukan nilai n : "))
    ```
  * lakukan perulangan dan variabel n sebagai batasan looping nya
  * jangan lupa **import random** untuk membangkitkan nilai random
  * variabel a untuk menyimpan batasan nilai <0.5
  * dan cetak nilai a 
  * ```
    for i in range(n):
        a = random.uniform(0.0, 0.5)
        print(a)
    ```
  




