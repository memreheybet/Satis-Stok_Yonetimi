from veritabani import db, cursor


def musteriList(cursor,db):
    cursor.execute('select * from Musteriler')
    musteriler = cursor.fetchall()
    print("Müşteri Listesi:")
    for musteri in musteriler:
        print(f"ID: {musteri[0]}, İsim: {musteri[1]}, Soyisim: {musteri[2]}")
    print("Müşteriler Listelendi")

