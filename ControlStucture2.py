a = int (input("Masukkan Angka pertama : "))
b = int (input("Masukkan Angka kedua: "))
c = int (input("Masukkan Angka ketiga: "))

if a > b and a > c :
    largest = a
    print ("Angka terbesar adalah : ", largest)
elif b > a and b > c :
    largest = b
    print ("Angka terbesar adalah : ", largest)
elif c > a and c>b:
    largest = c
    print ("Angka terbesar adalah : ", largest)
else:
    print ("Tidak ada angka terbesar")