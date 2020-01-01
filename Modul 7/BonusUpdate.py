import datetime
import time
print("Program menampilkan waktu komputer.")
date = datetime.datetime.now()
jam = date.hour
menit = date.minute
detik = date.second
while detik >= 0:
    if detik == 0 :
        print(str(jam) + ":" + str(menit) + ":" + str(detik) + "0")
        print("Jam pratikum sudah habis. Silakan pulang.")
        break
    else :
        print(str(jam) + ":" + str(menit) + ":" + str(detik))
        time.sleep(1)
        date = datetime.datetime.now()
        detik = date.second
        menit = date.minute
        jam = date.hour
