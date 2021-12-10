from datetime import*

def diffDate(x):
    tanggal = x.split("-")
    mylist = []

    for i in tanggal :
        mylist.append(int(i))

    dulu = date(mylist[0],mylist[1],mylist[2])    
    skr = datetime.date(datetime.now())

    a = dulu - skr
    hasil = (a.days)
    return hasil


print(diffDate('2018-12-30'))
print(diffDate('2021-01-20'))
    
try:
    x = input('Masukkan dengan format yyyy-mm-dd :')
    h = diffDate(x)
    print("Selisih tanggal {0} dengan hari ini adalah {1} hari".format(x,h))
    print("\nnb = (-) memiliki arti sudah lampau") 
except ValueError :
    print("input Invalid")

