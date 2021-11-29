mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

listbaru =[]

for i in range(len(mhs)):
    x = mhs [i].split(":")
    listbaru.append(x)

for z in range(len(listbaru)):
    y = listbaru[z][2].split('-')
    y.reverse()
    ybaru = '/'.join(y)
    listbaru[z][2] = ybaru

     
print("===================================================================")
print('NIM     NAMA MAHASISWA        TGL LAHIR      TEMPAT LAHIR   ')                                          
print("-------------------------------------------------------------------")


for i in range(len(listbaru)):
    print(listbaru[i][0].ljust(8), end='')
    print(listbaru[i][1].ljust(22), end='')
    print(listbaru[i][2].ljust(15), end='')
    print(listbaru[i][3].ljust(15))
print("-------------------------------------------------------------------")
