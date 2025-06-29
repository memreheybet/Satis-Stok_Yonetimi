from veritabani import cursor, db


def gunluk_rapor(cursor,db):
    try:
        cursor.execute("""
            SELECT 
                CAST(TARIH AS DATE) AS GUN,
                COUNT(S.ID) AS SATIS_SAYISI,
                SUM(S.ADET) AS TOPLAM_ADET,
                SUM(S.ADET * U.FIYAT) AS TOPLAM_CIRO
            FROM Satislar S
            JOIN Urunler U ON S.URUN_ID = U.ID
            GROUP BY CAST(TARIH AS DATE)
            ORDER BY GUN DESC;
        """)

        veriler = cursor.fetchall()

        print(" Günlük Satış Raporu:")
        print("---------------------")
        for row in veriler:
            gun, satis_sayisi, toplam_adet, toplam_ciro = row
            print(f"{gun} | Satış Sayısı: {satis_sayisi} | Adet: {toplam_adet} | Ciro: {toplam_ciro:.2f} TL")

    except Exception as e:
        print("Hata oluştu:", e)

#gunluk_rapor(cursor,db)