from veritabani import cursor, db


def aylik_rapor(cursor,db):
    cursor.execute("""
        SELECT 
            YEAR(TARIH) AS YIL,
            MONTH(TARIH) AS AY,
            COUNT(S.ID) AS SATIS_SAYISI,
            SUM(S.ADET) AS TOPLAM_ADET,
            SUM(S.ADET * U.FIYAT) AS TOPLAM_CIRO
        FROM Satislar S
        JOIN Urunler U ON S.URUN_ID = U.ID
        GROUP BY YEAR(TARIH), MONTH(TARIH)
        ORDER BY YIL DESC, AY DESC;
    """)

    veriler = cursor.fetchall()

    print("📅 Aylık Satış Raporu:")
    print("------------------------------")
    for satir in veriler:
        yil, ay, satis_sayisi, toplam_adet, toplam_ciro = satir
        print(f"{yil}-{ay:02d} | Satış Sayısı: {satis_sayisi} | Adet: {toplam_adet} | Ciro: {toplam_ciro:.2f} TL")
#aylik_rapor(cursor,db)