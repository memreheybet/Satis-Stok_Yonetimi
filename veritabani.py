import pypyodbc


db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=.;'
    'Database=Stok-Satıs_Yonetımı;'
    'Trusted_Connection=True;'
)
cursor = db.cursor()