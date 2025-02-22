class Mahasiswa :
    def __init__(self, nama, nim, jurusan, angkatan) :
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.angkatan = angkatan

    def tampilkan_mahasiswa(self) :
        print("Nama : ", self.nama)
        print("NIM : ", self.nim)
        print("Jurusan : ", self.jurusan)
        print("Angkatan : ", self.angkatan)

nama = input ("Masukkan Nama Mahasiswa : ")
nim = input ("Masukkan NIM Mahasiswa : ")
jurusan = input ("Masukkan Jurusan Mahasiswa : ")
angkatan = input ("Masukkan Angkatan Mahasiswa : ")

mahasiswa = Mahasiswa(nama, nim, jurusan, angkatan)

mahasiswa.tampilkan_mahasiswa()