from veritabani import cursor, db

from models import urunEkle_modeli

def urunEkle(cursor,db):
    URUN_ADI, FIYAT, STOK_MIKTARI= urunEkle_modeli()

    cursor.execute("INSERT INTO Urunler (URUN_ADI, FIYAT,STOK_MIKTARI) VALUES (?, ?, ?)",
                   (URUN_ADI, FIYAT, STOK_MIKTARI))
    db.commit()
    print("Yeni Ürün eklendi.")

#urunEkle(cursor,db)