print("Note: Masukkan 0 pada menu yang tidak dipesan")
Kopi=int(input("Kopi: "))
KopiSusu=int(input("Kopi Susu: "))
SusuPutih=int(input("Susu Putih:"))
SusuCoklat=int(input("Susu Coklat: "))

A= (Kopi*4500)
B= (KopiSusu*6000)
C= (SusuPutih*5000)
D= (SusuCoklat*6000)

TotalHarga = A+B+C+D

print(TotalHarga)
Bayar=int(input("Uang yang dibayar : "))
Kembalian= Bayar-TotalHarga
if Bayar > TotalHarga:
    print("Kembalian: ",Kembalian)
else :
    print("Uang pas")