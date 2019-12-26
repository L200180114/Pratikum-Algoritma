# Kegiatan Praktikum
### Kegiatan 1. Identitas
1. Buatlah program yang menampilkan identitas saudara, mulai dari Nama, Alamat, umur, dan lain-lain hingga minimal 10 data diri.
Pada program, setiap data harus disimpan dalam sebuah objek yang mempunyai nama. Berikut adalah contoh bagian awal program.
```
### Program Identitas diri. Dibuat oleh David L20000012
Nama = 'David Bohlam'
Alamat = ...
...
```
2. Setelah program dapat berjalan, tunjukan pada asisten.
### Kegiatan 2. Akun
1. Buatlah sebuah program yang baris pertama dan kedua dari program tersebut merupakan objek Nama dan Tanggal lahir saudara.
Berikut contohnya.
```
## Program Akun
## Dibuat oleh David L20000012
Nama = 'David John Bohlam'
TanggalLahir = '15 September 1990'
...
```
2. Lanjutkan program tersebut sehingga menampilkan Nama saudara, Tanggal Lahir, dan Nama singkat. Contoh nama singkat adalah : 
'D. J. Bohlam' Nama singkat harus diolah dari objek Nama. Jika nama saudara hanya terdiri atas sati kata, nama singkat sama
dengan nama lengkap.
3. Lanjutkan program tersebut sehingga menampilkan username dari sebuah sistem. Username dibuat dari inisial, tanggal dan tahun
lahir. Contoh username untuk David Bohlam adalah : 'D151990' karena lahir pada tanggal 15 tahun 1990. Username harus diolah dari
objek Nama dan TanggalLahir.
4. Lanjutkan program tersebut untuk membuat dan menampilkan *password* sementara. *Password* dibuat dengan mengambil 3 huruf pertama
dari Nama ditambah 3 angka acak. Misalnya *password* sementara untuk David Bohlam adalah Dav594.
5. Setelah program berjalan, tunjukkan pada asisten.
### Kegiatan 3.Operator
1. Ketikkan perintah-perintah berikut ini pada mode interatif. Pada program tersebut, gantilah data untuk data Nama dan NIM sesuai
identitas saudara.
```
1  >>> Nama = 'David John Bohlam' # ganti dg nama saudara
2  >>> NIM = 'L200100100 # ganti dengan NIM saudara
3  >>> X = '1' + NIM[7:]
4  >>> a = int(X) # konversi string ke integer
5  >>> b = len(Nama)
```
2. Lanjutkan program di atas dengan menuliskan perintah-perintah di bawah ini. Setiap kali satu perintah dikerjakan, tuliskan
respon dari Python. Tuliskan juga komentar pada lembar kerja mengapa Python memberi respon seperti itu.
```
6  >>> type(a)
7  >>> type(b)
8  >>> a / b
9  >>> a // b
10 >>> 10 * (a - 999)
11 >>> b ** 2
12 >>> a % b
```
3. Lanjutkan program di atas dengan menuliskan perintah-perintah di bawah ini. Setiap kali satu perintah dikerjakan, tuliskan
respon dari Python. Tuliskan juga komentar pada lembar kerja mengapa Python memberi respon seperti itu.
```
13 >>> c = 12.5
14 >>> type(c)
15 >>> a / c
16 >>> a // c
17 >>> a % c
```
4. Lanjutkan program di atas dengan menuliskan perintah-perintah di bawah ini. Setiap kali satu perintah dikerjakan, tuliskan
respon dari Python. Tuliskan juga komentar pada lembar kerja mengapa Python memberi respon seperti itu.
```
18 >>> c > b
19 >>> type(c > b)
20 >>> a > b and b > c
21 >>> a > 1100 or b < 10
```
### Kegiatan 4. Tipe Data
1. Ketikkan perintah-perintah berikut ini pada mode interaktif. Pada program tersebut, gantilah NIM dengan tiga digit terakhir
NIM saudara. Catatan: jika digit ke-8 dari NIM saudara adalah 0 maka tambahkan satu digit lagi di depannya yaitu angka 1.
```
1  >>> Nama = 'David John Bohlam' # ganti dg nama saudara
2  >>> NIM = 127      # tiga digit terakhir NIM saudara
3  >>> Tinggi = 1.71  # tinggi saudara dalam satuan meter
4  >>> Berat = 65     # ganti dg berat badan saudara
5  >>> TahunLahir = 1990  # ganti dg tahun lahir saudara
6  >>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
7  >>> Data = (TahunLahir, Berat, Tinggi, NIM, Nama)
```
2. Lanjutkan program di atas dengan menuliskan perintah-perintah dibawah ini. Setiap kali satu perintah dikerjakan, tuliskan
respon dari Python. Tuliskan juga komentar pada lembar kerja mengapa Python memberi respon seperti itu.
```
8  >>> type(Aku)
9  >>> Aku[0]
10 >>> a = NIM % 4; Aku[a]
11 >>> type(Aku[a])
12 >>> Aku[a:4]
13 >>> type(Aku[4])
14 >>> Aku[0] == 'ok'
```
3. Lanjutkan program di atas dengan menuliskan perintah-perintah di bawah ini. Setiap kali sati perintah dikerjakan, tuliskan
respon dari Python. Tuliskan juga komentar pada lembar kerja mengapa Python memberi respon seperti itu.
```
15 >>> type(Data)
16 >>> type(Data[4])
17 >>> Data[4][5]
18 >>> Data[4][a:6]
19 >>> Data[0] = 'ok'; Data
20 >>> Data[-1]
21 >>> range(a)
```
