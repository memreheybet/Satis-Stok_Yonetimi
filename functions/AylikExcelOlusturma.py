import datetime
import os
from openpyxl import Workbook
from veritabani import db, cursor


def aylik_rapor_excel(cursor, db):
    cursor.execute("""
        SELECT 
            YEAR(TARIH) AS YIL,
            MONTH(TARIH) AS AY,
            COUNT(S.ID) AS SATIS_SAYISI,
            SUM(S.ADET) AS TOPLAM_ADET,
            SUM(S.ADET * U.FIYAT) AS TOPLAM_CIRO
        FROM Satislar S
        JOIN URUNLER U ON S.URUN_ID = U.ID
        GROUP BY YEAR(TARIH), MONTH(TARIH)
        ORDER BY YIL DESC, AY DESC;
    """)

    veri = cursor.fetchall()

    wb = Workbook()
    ws = wb.active
    ws.title = "Aylık Rapor"

    basliklar = ["Yıl", "Ay", "Satış Sayısı", "Toplam Adet", "Toplam Ciro (TL)"]
    ws.append(basliklar)

    for satir in veri:
        yil, ay, satis_sayisi, toplam_adet, toplam_ciro = satir
        ws.append([yil, ay, satis_sayisi, toplam_adet, round(float(toplam_ciro), 2)])

    # Klasör oluştur ve dosya adını belirle
    os.makedirs("Aylik Raporlar", exist_ok=True)
    tarih_str = datetime.datetime.now().strftime("%Y-%m")
    dosya_adi = os.path.join("Aylik Raporlar", f"aylik_satis_raporu_{tarih_str}.xlsx")

    wb.save(dosya_adi)
    print(f"Aylık rapor başarıyla kaydedildi: {dosya_adi}")


if __name__ == "__main__":
    aylik_rapor_excel(cursor, db)
