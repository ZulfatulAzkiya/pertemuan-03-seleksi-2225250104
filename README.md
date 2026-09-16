# Pertemuan 03 Seleksi Python
Nama: Zulfatul Azkiya
NIM: 2225250104
Kelas: 3A

## Tujuan
Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

Menerapkan konsep seleksi dalam beberapa latihan serta membuat program analisis persamaan kuadrat menggunakan nested if.

## Pembahasan
Pada pertemuan ini terdapat beberapa latihan mengenai struktur seleksi pada Python.

1. Latihan Genap dan Ganjil
   Program digunakan untuk menentukan apakah suatu bilangan merupakan bilangan genap atau ganjil. Penentuan dilakukan dengan menggunakan operator modulus (%).

2. Latihan Membandingkan Dua Bilangan
   Program digunakan untuk membandingkan dua bilangan dan menentukan apakah bilangan pertama lebih besar, lebih kecil, atau sama dengan bilangan kedua.

3. Latihan Kelulusan Bersyarat
   Program digunakan untuk menentukan kelulusan berdasarkan nilai akhir dan persentase kehadiran. Mahasiswa dinyatakan lulus jika nilai minimal 60 dan kehadiran minimal 80%.

4. Latihan Jenis Segitiga
   Program digunakan untuk menentukan jenis segitiga berdasarkan tiga panjang sisi. Program juga memeriksa apakah ketiga sisi dapat membentuk segitiga.

5. Tugas Analisis Persamaan Kuadrat
   Program digunakan untuk menganalisis persamaan kuadrat dengan bentuk:

   ax² + bx + c = 0

   Program menggunakan diskriminan:

   D = b² - 4ac

   Berdasarkan nilai diskriminan, program menentukan apakah persamaan mempunyai dua akar real berbeda, satu akar real kembar, atau tidak mempunyai akar real.

## Cara Menjalankan
Untuk menjalankan program latihan:

python3 latihan/01_genap_ganjil.py

python3 latihan/02_bandingkan_dua_bilangan.py

python3 latihan/03_kelulusan_bersyarat.py

python3 latihan/04_jenis_segitiga.py

Untuk menjalankan program tugas:

python3 tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas
1. Baca nilai a, b, dan c sebagai float.
2. Periksa apakah a sama dengan 0.
3. Jika a = 0, tampilkan bahwa input bukan persamaan kuadrat.
4. Jika a tidak sama dengan 0, hitung diskriminan dengan rumus D = b ** 2 - 4 * a * c.
5. Periksa apakah D lebih besar dari 0.
6. Jika D > 0, hitung dua akar real berbeda.
7. Jika D = 0, hitung satu akar real kembar.
8. Jika D < 0, tampilkan bahwa tidak ada akar real.
9. Tampilkan nilai numerik dengan dua angka di belakang koma.

## Hasil Pengujian

### Test Case 1
Input:
a = 1
b = -5
c = 6

Keluaran yang diharapkan:
Dua akar real: 3.00 dan 2.00

Keluaran aktual:
Dua akar real: 3.00 dan 2.00

Status: Berhasil

### Test Case 2
Input:
a = 1
b = 2
c = 1

Keluaran yang diharapkan:
Akar kembar: -1.00

Keluaran aktual:
Akar kembar: -1.00

Status: Berhasil

### Test Case 3
Input:
a = 1
b = 0
c = 1

Keluaran yang diharapkan:
Tidak ada akar real.

Keluaran aktual:
Tidak ada akar real.

Status: Berhasil

### Test Case 4
Input:
a = 0
b = 2
c = 3

Keluaran yang diharapkan:
Bukan persamaan kuadrat.

Keluaran aktual:
Bukan persamaan kuadrat.

Status: Berhasil

## Refleksi
Kesalahan logika yang ditemukan adalah program dapat mengalami kesalahan jika langsung menghitung akar tanpa memeriksa nilai a terlebih dahulu.

Jika a = 0, maka input bukan merupakan persamaan kuadrat. Cara memperbaikinya adalah dengan memeriksa kondisi a == 0 terlebih dahulu sebelum menghitung diskriminan dan akar.

Penggunaan nested if digunakan untuk menentukan tiga kemungkinan nilai diskriminan, yaitu D > 0, D = 0, dan D < 0.

Dari tugas ini, saya memahami bahwa struktur seleksi dapat digunakan untuk membuat keputusan berdasarkan kondisi tertentu pada sebuah program Python.