class Praktikum :
    def __init__(self, nama, nim, kelas) :
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
    
    def tampilkan_kelas(self) :
        print("Nama : " + self.nama)
        print("NIM : " + self.nim)
        print("Kelas : " + self.kelas)

nama = input ("Masukkan Nama Mahasiswa : ")
nim = input ("Masukkan NIM Mahasiswa : ")
kelas = input ("Masukkan Kelas Praktikum Mahasiswa : ")

prak = Praktikum(nama, nim, kelas)

prak.tampilkan_kelas()