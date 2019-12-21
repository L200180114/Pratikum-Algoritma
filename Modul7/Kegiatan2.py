password = "Arga"
inputpass = str(input("Masukkan password: "))
i = 0
while i <= 3 :
    if i == 2 :
        print("Anda telah mencoba 3 kali. Akses ditolak.")
        break
    elif inputpass != password:
        inputpass = str(input("Maaf, anda salah memasukkan password. Masukkan password: "))
    elif inputpass == password:
        print("Anda berhasil login")
        break
    i = 1 + i
