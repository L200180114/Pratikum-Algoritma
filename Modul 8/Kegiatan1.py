identitas = {'nama':'Arga Dwi Ardinata', 'nim':'L200180114', 'alamat':'Jenggrik, Kedunggalar, Ngawi', 'kodepos':'23145', 'bantuan':'Pilihan yang tersedia:\nb menampilkan bantuan ini\nN menampolkan NIM\na menampilkan Nama\nA menampilkan Alamat\nK menampilkan Kode pos\nx xxx\nx xxx\nx xxx\nk keluar\n'}
print(identitas['bantuan'])
a = str(input("Pilihan saudara: "))
while a != "stop":
    if a == "k":
        print("Terima kasih.")
        break
    elif a == "N":
        print("NIM: " + identitas['nim'] + "\n")
    elif a == "a":
        print("Nama: " + identitas['nama'] + "\n")
    elif a == "A":
        print("Alamat: " + identitas['alamat'] + "\n")
    elif a == "K":
        print("Kode pos: " + identitas['kodepos'] + "\n")
    elif a == "b":
        print(identitas['bantuan'])
    a = str(input("Pilihan saudara: "))
