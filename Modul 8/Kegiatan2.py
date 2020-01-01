def konversiSuhu(C = 0, F = 0):
    if C == 0 and F == 0 :
        print("Suhu 0 Celcius setara dengan 32 Fahrenheit")
    elif C == 0 :
        hasil = (F - 32)*(5/9)
        print("Suhu", F, "Farenheit setara dengan", int(hasil), "Celcius")
    elif F == 0 :
        hasil = (C * (9/5)) + 32
        print("Suhu", C, "Celcius setara dengan", int(hasil), "Farenheit")
