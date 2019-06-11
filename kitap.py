class KitapKayit:

    def __init__(self, KayitDosyasi = "Kitap.txt"):
        self.DosyaAdi = KayitDosyasi
        self.Eserler = []
        self.Yazarlar = []
        self.Yillar = []
        return

    def YeniKitap(self, EserAdi, Yazar, Yil):
        self.Eserler.append(EserAdi)
        self.Yazarlar.append(Yazar)
        self.Yillar.append(Yil)
        self.KayitEt()
        return

    def KayitOku(self):
        try:
            with open(self.DosyaAdi, "r") as dosya:
                EserSayisi = int(dosya.readline())
                for x in range(EserSayisi):
                    self.Eserler.append(dosya.readline()[:-1])
                    self.Yazarlar.append(dosya.readline()[:-1])
                    self.Yillar.append(dosya.readline()[:-1])
            return True
        except FileNotFoundError:
            return False

    def KayitEt(self):
        with open(self.DosyaAdi, "w") as dosya:
            dosya.write(str(len(self.Eserler)) + "\n")
            for x in range(len(self.Eserler)):
                dosya.write(self.Eserler[x]+ "\n")
                dosya.write(self.Yazarlar[x]+ "\n")
                dosya.write(self.Yillar[x]+ "\n")

    def HepsiniGoster(self):
        if len(self.Eserler) == 0:
            print("Kayıtta Eser Bulunmamaktadır.")
        for x in range(len(self.Eserler)):
            print("Eser Adı:", self.Eserler[x],
                  "Yazar:", self.Yazarlar[x],
                  "Yayın Yılı:", self.Yillar[x])
            print()

    def SeciliGoster(self, index):
        if type(index) is int:
            index = [index]
        if len(index) == 0:
            print("Gösterilecek kayıt yoktur.")
        for x in index:
            print("Eser Adı:", self.Eserler[x],
                  "Yazar:", self.Yazarlar[x],
                  "Yayın Yılı:", self.Yillar[x])
            print()

    def Ara(self, liste, aranacak):
        eslesme = []
        for x in range(len(liste)):
            if liste[x].lower() == aranacak.lower():
                eslesme.append(x)
        return eslesme


    def YilAra(self, yil):
        yil = yil
        return self.Ara(self.Yillar, yil)

    def YazarAra(self, yazar):
        return self.Ara(self.Yazarlar, yazar)

    def EserAra(self, eser):
        return self.Ara(self.Eserler, eser)
