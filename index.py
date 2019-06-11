from kitap import KitapKayit

KK = KitapKayit()

def KesitBas():
    print()
    print("----------------------------------")
    print()

def cevapal(bas, son):
    cevap = input("Seçiminizi Giriniz:")
    try:
        cevap = int(cevap)
    except ValueError:
        print("Lütfen Bir sayı giriniz.")
        return cevapal(bas, son)
    if not cevap >= bas or not cevap <= son:
        print("Lütfen menüde olan bir değer giriniz.")
        return cevapal(bas, son)
    return cevap

def basla():
    print("KÜTÜPHANEME HOŞGELDİNİZ")
    print("Menülerde yanıtlarınızı lütfen sayılar ile veriniz")
    if not KK.KayitOku():
        print(KK.DosyaAdi, "bulunamadı. Sisteme veri yüklenmedi.")
    menu()
    return


def menu():
    KesitBas()
    print("Ne yapmak istersiniz:")
    print("1) Kayıtları Görmek")
    print("2) Yeni Kayıt Eklemek")
    print("3) Eser Araması")
    cevap = cevapal(1,3)
    if cevap == 1:
        KayitListele()
    elif cevap == 2:
        KesitBas()
        print("Kayıt Ekleniyor.")
        KayitEkle()
    elif cevap == 3:
        EserArama()
    return

def KayitEkle():
    Eser = input("Lütfen eser adı giriniz:")
    Yazar = input("Lütfen yazar adı giriniz:")
    Yil = input("Lütfen yayın yılı giriniz:")
    if Eser == "" or Yazar == "" or Yil == "":
        print("Kayıt bilgileri boş bırakılamaz.")
        return KayitEkle()
    KK.YeniKitap(Eser, Yazar, Yil)
    print("Kayıt Eklendi.")
    menu()
    return

def KayitListele():
    KesitBas()
    print("Kayıtların Hepsi Gösteriliyor.")
    KK.HepsiniGoster()
    input("Devam etmek için enter'a basın...")
    menu()
    return

def EserArama():
    print("Hangi kritere göre eser aramak istersiniz:")
    print("1) Eser Adı")
    print("2) Yazar Adı")
    print("3) Yayın yılı")
    cevap = cevapal(1,3)
    arama = input("Aranacak anahtar kelime:")
    if cevap == 1:
        sonuc = KK.EserAra(arama)
    elif cevap == 2:
        sonuc = KK.YazarAra(arama)
    elif cevap == 3:
        sonuc = KK.YilAra(arama)
    print("Sonuç Gösteriliyor.")
    KK.SeciliGoster(sonuc)
    input("Devam etmek için enter'a basın...")
    menu()
    return

basla()
