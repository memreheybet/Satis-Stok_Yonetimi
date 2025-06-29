import datetime
import os
from openpyxl import Workbook
from veritabani import db, cursor

def gunluk_rapor_excel(cursor, db):
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

    wb = Workbook()
    ws = wb.active
    ws.title = "Günlük Rapor"

    basliklar = ["Gün", "Satış Sayısı", "Toplam Adet", "Toplam Ciro (TL)"]
    ws.append(basliklar)

    for satir in veriler:
        gun, satis_sayisi, toplam_adet, toplam_ciro = satir
        ws.append([str(gun), satis_sayisi, toplam_adet, round(float(toplam_ciro), 2)])

    tarih_str = datetime.datetime.now().strftime("%Y-%m-%d")

    # Raporlar klasörü oluşturuluyor
    os.makedirs("Gunluk Raporlar", exist_ok=True)
    dosya_adi = os.path.join("Gunluk Raporlar", f"gunluk_satis_raporu_{tarih_str}.xlsx")

    wb.save(dosya_adi)
    print(f"Günlük rapor başarıyla kaydedildi: {dosya_adi}")

if __name__ == "__main__":
    gunluk_rapor_excel(cursor, db)
