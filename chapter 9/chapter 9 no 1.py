# nomor 1

# cara 1

def ubahhuruf(teks,a,b):
    teks = list(teks)
    for i in range(len(teks)):
        if(teks[i] == a):
            teks[i] = b
    ganti = ''.join(teks)
    return ganti

# cara 2

def ubahhuruf(teks,a,b):
    ubah = teks.replace(a,b)
    return ubah

teks = input('Masukkan kata yang ingin kamu ubah :')
a = input('huruf apa yang ingin kamu ubah :')
b = input('ingin kamu ubah {} dengan huruf apa ? :'.format(a))

hasil = ubahhuruf(teks,a,b)
print("Hasilnya :",hasil)
