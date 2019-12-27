nama = str(input("Masukkan nama saudara: "))
waktu = float(input("Pukul berapa sekarang? "))
if waktu >= 06.00 and waktu <= 09.00 :
    print("Selamat pagi " + nama)
elif waktu >= 09.01 and waktu <= 11.59 :
    print("Selamat menjelang siang " + nama)
elif waktu >= 12.00 and waktu <= 14.59 :
    print("Selamat siang " + nama)
elif waktu >= 15.00 and waktu <= 17.59 :
    print("Selamat sore " + nama)
elif waktu >= 18.00 and waktu <= 24.00 :
    print("Selamat malam " + nama)
elif waktu >= 00.00 and waktu <= 05.59 :
    print("Selamat dini hari " + nama)
