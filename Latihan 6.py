class Manusia :
    def __init__(self, nama, umur) :
        self.nama = nama
        self.umur = umur

    def tampilkan_manusia(self) :
        print("Nama : ", self.nama )
        print("Umur : ", self.umur )

nama = input("Masukkan Nama Anda : ")
umur = int(input("Masukkan Umur Anda : "))

data = Manusia(nama, umur)

data.tampilkan_manusia() 