class AddTanya:
    def __init__(self, cls):
        self.cls = cls
    
    def __call__(self, bertanya):
        instance = self.cls(bertanya)

        def tanya():
            print(f"Hallo, Berapa {instance.bertanya} Anda?")
        instance.tanya = tanya
        return instance

@AddTanya
class Pertanyaan:
    def __init__(self, bertanya):
        self.bertanya = bertanya

pertanyaan = Pertanyaan("Umur")
pertanyaan.tanya()
