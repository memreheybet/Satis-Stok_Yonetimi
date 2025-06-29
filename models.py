from sys import int_info


def musteriEkle_modeli():
    ISIM=input("ISIM: ")
    SOYISIM = input("Soyismini Giriniz: ")
    return ISIM, SOYISIM
def musteriSil_modeli():
    musteri_id = int(input("Silinecek IDyi Giriniz: "))
    return musteri_id

def urunEkle_modeli():
    ISIM = input("Urun Ismi Giriniz: ")
    FIYAT = int(input("FIYAT Giriniz: "))
    STOK_MIKTARI = int(input("Stok Miktari Giriniz: "))
    return ISIM, FIYAT, STOK_MIKTARI

def urunSil_modeli():
    URUN_ID = int(input("Silinecek Ürünün ID sini Giriniz: :"))
    return URUN_ID

def satis_modeli():
    musteriID = int(input("Müşteri ID'sini Giriniz: "))
    urunID = int(input("Uruni ID'sini Giriniz: "))
    adet = int(input("Kaç Adet Satın Aldı: "))
    return musteriID,urunID,adet

def stokkontrol_Modeli():
    urunid = int(input("Ürün Id'sini Giriniz"))
    return urunid

