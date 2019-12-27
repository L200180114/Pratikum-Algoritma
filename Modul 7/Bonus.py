import datetime
import time
print("Program menampilkan waktu komputer.")
date = datetime.datetime.now()
jam = date.hour
menit = date.minute
detik = date.second
while detik >= 0:
    if detik == 60 :
        menit = menit + 1
        detik = 0
        print(str(jam) + ":" + str(menit) + ":" + str(detik) + "0")
        print("Jam pratikum sudah habis. Silakan pulang.")
        break
    else :
        print(str(jam) + ":" + str(menit) + ":" + str(detik))
        detik = detik + 1
        time.sleep(1)
    
