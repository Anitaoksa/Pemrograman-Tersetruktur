# nomor 5

nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	{'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
        {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
        {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	{'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]


print("=======================================================================================")
print("NIM      NAMA              N.MID         N.UAS            N.AKHIR    STATUS           ")
print("---------------------------------------------------------------------------------------")

for i in range(len(nilai)):
    akhir = int(nilai[i]["mid"] + (2*nilai[i]["uas"])/3)

    if (akhir >= 60):
        status = 'LULUS'
    else :
        status == 'TIDAK LULUS'
        
    print(nilai[i]["nim"].ljust(9), end='')
    print(nilai[i]["nama"].ljust(18), end='')
    print(str(nilai[i]["mid"]).ljust(14), end='')
    print(str(nilai[i]["uas"]).ljust(17), end='')
    print(str(akhir).ljust(13), end='')
    print(str(status).ljust(15), end='')

    

print("---------------------------------------------------------------")

