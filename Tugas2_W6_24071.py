from abc import ABC, abstractmethod

class Book(ABC):
    @abstractmethod
    def halaman(self):
        pass

    @abstractmethod
    def genre(self):
        pass

class Bumi(Book):
    judul = "Bumi"
    def halaman(self):
        return 440
    
    def genre(self):
        return "Fiksi"

class Madilog(Book):
    judul = "Madilog"
    def halaman(self):
        return 560
    
    def genre(self):
        return "Non Fiksi"

bumi = Bumi()
madilog = Madilog()

print(f"Judul Buku = {bumi.judul}, Jumlah Halaman = {bumi.halaman()}, Genre Buku = {bumi.genre()}")
print(f"Judul Buku = {madilog.judul}, Jumlah Halaman = {madilog.halaman()}, Genre Buku = {madilog.genre()}")
