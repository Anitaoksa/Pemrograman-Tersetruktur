print ("=== Cek Tarif Klaten Rental Mobil ===")
print ("butuh mobil?, rental aja di klatenrental.com")
# import library
import time
import datetime
# hitung lama rental
mulai =  float(input("mulai rentalnya jam berapa nih ?"))
selesai = float(input("selesai jam berapa ni rentalnya tadi?,jangan bo'ong"))
lamarental = selesai-mulai
print("lama rental Anda adalah =",round(lamarental), "jam")
# tampilkan tarif sesuai lama rental
tarif = 200000
if (lamarental <= 12) :
	print ("Tagihan Anda = Rp", tarif)
	print ("Terima kasih")
if (lamarental >12) :
	tarif_selanjutnya = tarif + ((lamarental - 12)*10000)
	print("Tagihan Anda = Rp", tarif_selanjutnya)
	print("Terima kasih")
