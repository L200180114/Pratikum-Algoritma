print("Program menampilkan waktu komputer.")
jam = 6
menit = 12
detik = 10
while detik >= 0:
    if detik == 60 :
        detik = detik - 60
        menit = 1 + menit
        print(str(jam) + ":" + str(menit) + ":" + str(detik) + "0")
        print("Jam pratikum sudah habis. Silakan pulang.")
        break
    else :
        print(str(jam) + ":" + str(menit) + ":" + str(detik))
        detik = 1 + detik
    
