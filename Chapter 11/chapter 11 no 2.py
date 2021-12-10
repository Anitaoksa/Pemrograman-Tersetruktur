import os
from datetime import*

if (os.path.exists):
    mode = 'a+'
else :
    mode = 'w'
    
file = open('e:\python1.txt',mode)

while True :
    kode = input("Masukkan Kode Member :")
    nama = input("Masukkan Nama Member :")
    judul = input("Masukkan Judul Buku :")

    today = datetime.date(datetime.now())
    kembali = today + timedelta(days = 7)

    file.write(kode + "|" + nama + "|" + judul + "|" + str(today) + "|" + str(kembali) + "\n")

    i= input("lagi? (y/n) :".lower())
    
    if (i == 'y'):
        continue
    
    elif (i == 'n'):
        file.close
        break

    else:
        print("input Invalid")
        break
    
baca = open('e:\python1.txt','r')    
file.seek(0,0)
lagi = file.read()
print ("Baik, Terima kasih berikut rekapannya", lagi)


