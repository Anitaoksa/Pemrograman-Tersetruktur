# nomor 2

def baris(n):
    space = 2*n-1
    for i in range(n):
        print(("*"*(2*i-1)).center(space))

baris(5)
