from datetime import*
import PythonProjectChapter11_1

file = open('e:\python1.txt','r')
line = file.readlines()

kode = input('Masukkan Kode Member :')

datamember = {}
try:
    for i in range(len(line)):
        if (kode in line [i]):
            a = line[i].replace('\n','')
            b = a.split('|')

            datamember[kode] = [b[1], b[2], b[3], b[4]]

    print("\nDATA PEMINJAMAN BUKU")
    print("Kode Member               :", kode)
    print("Nama Member               :", datamember[kode][0])
    print("Judul Buku                :", datamember[kode][1])
    print("Tanggal Mulai Peminjaman  :", datamember[kode][2])
    print("Tanggal Maks Peminjaman   :", datamember[kode][3])

    balik = print("Tanggal Pengembalian      :", datetime.date(datetime.now()))

    telat = PythonProjectChapter11_1.diffDate(datamember[kode][3])
    denda = 2000* abs(telat)
                  
    if(telat >= 0):
        print("Terlambat    :0 hari")
        print("Denda        : Rp. 0")

    else :
        print("Terlambat    :", abs(telat), "hari")
        print("Denda        : Rp.", denda)
        
except KeyError:
    print("Data Tidak Ditemukan")
