class Persegi :
    def __init__(self, sisi) :
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self) :
        return self.sisi * 4
    
sisi_persegi = (int(input("Masukkan Sisi Persegi : ")))
hasil = Persegi(sisi_persegi)
    
print("Luas Persegi Adalah : ", hasil.luas())
print("Keliling Persegi Adalah : ", hasil.keliling())