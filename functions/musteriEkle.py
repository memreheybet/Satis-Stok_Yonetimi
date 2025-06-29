from veritabani import db, cursor
from models import musteriEkle_modeli

def musteriEkleme(cursor,db):
    ISIM, SOYISIM =musteriEkle_modeli()
    cursor.execute("INSERT INTO Musteriler (ISIM, SOYISIM) VALUES (?, ?)",
                   (ISIM, SOYISIM))
    db.commit()
    print("Müşteri eklendi.")
#musteriEkleme(cursor,db)