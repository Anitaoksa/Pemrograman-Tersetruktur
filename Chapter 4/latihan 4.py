print ("Jawablah soal berikut!")
print ("4. Pak Amir menempuh perjalanan dari kota A ke B berjarak 125 km dengan rata-rata kecepatan 62 km/jam. Kemudian, dia melanjutkan perjalanan ke kota C berjarak 256 km dari kota B dengan kecepatan rata-rata 70 km/jam. Jika pak Amir berangkat dari kota A pukul 06.00, dan sempat istirahat di kota B selama 45 menit, maka tentukan pukul berapa pak Amir sampai di kota C!")
print ("jawab :")
print ("diketahui")
AB = 125
print ("AB = 125")
VAB = 62
print ("VAB = 62")
BC = 256
print ("BC = 256")
VBC = 70
print ("VBC = 70")
istirahat = 0.45
print ("istirahat = 45")
berangkat = 06.00
print ("berangkat = 06.00")

# menghitung waktu sampaiB
keB = AB/VAB
print ("keB = AB/VAB")
print (keB)
sampaiB = round (berangkat + keB)
print ("sampaiB = berangkat + keB")
print ("pak Amir sampai kota B pada pukul",sampaiB)

# menghitung waktu sampaiC
keC = BC / VBC
print ("keC = BC / VBC")
print (keC)
sampaiC = (sampaiB + keC + istirahat)
print ("sampaiC = (sampaiB + keC + istirahat)")
print (sampaiC)
print (round(sampaiC))
print ("jadi pak Amir akan sampai di kota C pada pukul",round(sampaiC))





