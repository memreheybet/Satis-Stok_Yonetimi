from selectors import SelectSelector

from functions.AylikExcelOlusturma import aylik_rapor_excel
from veritabani import db, cursor
from functions.GunlukExcelOlusturma import gunluk_rapor_excel
from functions.UrunSil import urunSilme
from functions.musteriEkle import musteriEkleme
from functions.musteriSil import musteriSilme
from functions.raporAylik import aylik_rapor
from functions.raporGunluk import gunluk_rapor
from functions.satis import satis_
from functions.stokKontrol import stokKontrolu
from functions.urunEkle import urunEkle
from functions.musteriler import musteriList

# === MENÜ ===
while True:
    print("\n--- MENÜ ---")
    print("1. Müşteri Ekle")
    print("2. Musteri Sil")
    print("3. Urun Ekle")
    print("4. Urun Sil")
    print("5. Stok Kontrolü")
    print("6. Satış Yap")
    print("7. Günlük Rapor Olustur")
    print("8. Aylık Rapor Olustur")
    print("9. Günlük Excel Raporu Olustur")
    print("10. Aylık Excel Raporu Olustur")
    print("+. Musteriler Listesi")
    print("0. Cikis")



    secim = input("Seçiminizi girin: ")

    if secim == "1":
        musteriEkleme(cursor,db)
    elif secim == "2":
        musteriSilme(cursor,db)
    elif secim == "3":
        urunEkle(cursor,db)
    elif secim == "4":
        urunSilme(cursor,db)
    elif secim == "5":
        stokKontrolu(cursor,db)
    elif secim == "6":
        satis_(cursor,db)
    elif secim == "7":
        gunluk_rapor(cursor,db)
    elif secim == "8":
        aylik_rapor(cursor,db)
    elif secim == "9":
        gunluk_rapor_excel(cursor,db)
    elif secim == "10":
        gunluk_rapor_excel(cursor, db)
    elif secim == "+":
        musteriList(cursor,db)
    elif secim == "0":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")


db.close()

