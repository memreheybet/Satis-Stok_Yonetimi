from tkinter.tix import InputOnly

from functions.musteriSil import musteriSilme
from models import urunSil_modeli
from veritabani import db, cursor

def urunSilme(cursor,db):
    urun_id= urunSil_modeli()
    cursor.execute('SELECT * FROM URUNLER WHERE ID = ?', (urun_id,))
    sonuc = cursor.fetchone()

    if sonuc:
        cursor.execute('UPDATE URUNLER SET DURUM=0  WHERE ID = ?', (urun_id,))
        db.commit()
        print("Girilen Urun Silindi")
    else:
        print("Girdiğin Ürün Bulunamadı")
#urunSilme(cursor,db)