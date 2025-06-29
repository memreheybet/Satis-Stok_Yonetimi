from veritabani import db, cursor
from models import musteriSil_modeli


def musteriSilme(cursor,db):
    musteri_id = musteriSil_modeli()
    cursor.execute('SELECT * from Musteriler where ID=?' , (musteri_id,))
    sonuc = cursor.fetchone()

    if sonuc:
        cursor.execute('UPDATE Musteriler SET AKTIF=0 where ID=?', (musteri_id,))
        db.commit()
        print("Müşteri Başarıyla Silindi")
    else:
        print("Girdiğiniz Müşteri Bulunamadı")
#musteriSilme(cursor,db)