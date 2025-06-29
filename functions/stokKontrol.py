from models import stokkontrol_Modeli
from veritabani import db, cursor


def stokKontrolu(cursor,db):
    urunid= stokkontrol_Modeli()
    cursor.execute("select STOK_MIKTARI from Urunler where ID = ?", (urunid,))
    sonuc=cursor.fetchone()

    if sonuc:
        stok_miktari = sonuc[0]
        print(f"Stok Miktarı: {stok_miktari}")
        if stok_miktari <= 10:
            print("Stok Seviyesi Kritik Seviyede. Tedarik Gerekli")
    else:
        print("Ürün Bulunamadı")
#stokKontrolu(cursor,db)