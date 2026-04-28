import pyodbc

server = r'LAPTOP-Q5MO66SO\SQLEXPRESS'   
database = 'CustomerShoppingDB'

conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

cursor = conn.cursor()
cursor.execute("SELECT DB_NAME()")
row = cursor.fetchone()

print("Connected successfully to:", row[0])

conn.close()