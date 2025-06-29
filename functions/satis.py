from models import satis_modeli
from veritabani import cursor, db


def satis_(cursor,db):
    musteriID, urunID, adet= satis_modeli()

    cursor.execute("SELECT STOK_MIKTARI FROM Urunler WHERE ID = ?", (urunID,))
    sonuc = cursor.fetchone()

    if not sonuc:
        print("Hatalı ID yazdınız... Lütfen Kontrol Ediniz")
        return
    mevcut_stok=sonuc[0]

    if adet > mevcut_stok:
        print(f"Stok Sayınız Yetersiz Eldeki Stok Sayısı: {mevcut_stok}")
        return


    cursor.execute("""
        INSERT INTO Satislar (Musterı_ID,Urun_ID,Adet) 
        VALUES (?,?,?)
    """,(musteriID,urunID,adet))

    cursor.execute("""
        update URUNLER 
        set STOK_MIKTARI= STOK_MIKTARI-?
        where ID =?
        """,(adet,urunID))
    db.commit()

    print("Satış Başarıyla Yapıldı. Stok Miktarı Güncellendi")
#satis_(cursor,db)