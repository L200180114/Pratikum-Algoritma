## Nama bangun dan rumus dimasukkan ke dalam dictionary
NamaBangun = {'nb1':'Segitiga', 'nb2':'Persegi', 'nb3':'Persegi Panjang', 'nb4':'Lingkaran', 'nb5':'Jajarang genjang'}
RumusLuas = {'segitiga':'L = 0.5 * a * t', 'persegi':'L = s ** 2', 'persegipanjang':'L = p * l', 'lingkaran':'L = pi * r ** 2', 'jajarangenjang':'L = a * t'}
print("No   | Nama bangun          | Rumus Luas")
print("-----|----------------------|--------------------")
print("1    |", NamaBangun['nb1'], "            |", RumusLuas['segitiga'])
print("2    |", NamaBangun['nb2'], "             |", RumusLuas['persegi'])
print("3    |", NamaBangun['nb3'], "     |", RumusLuas['persegipanjang'])
print("4    |", NamaBangun['nb4'], "           |", RumusLuas['lingkaran'])
print("5    |", NamaBangun['nb5'], "    |", RumusLuas['jajarangenjang'])
