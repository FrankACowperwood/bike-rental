import sqlite3

connection = sqlite3.connect("bike_rental.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bicycles (
    id INTEGER PRIMARY KEY,
    brand TEXT NOT NULL,
    type TEXT NOT NULL,
    price INTEGER NOT NULL,
    status TEXT NOT NULL
)
""")
cursor.execute("""
INTO bicycles (id, brand, type, price, status)
VALUES (1, 'Trek', 'mountain', 500, 'available')
""")

cursor.execute("""
INTO bicycles (id, brand, type, price, status)
VALUES (2, 'Cube', 'road', 400, 'available')
""")

cursor.execute("""
INTO bicycles (id, brand, type, price, status)
VALUES (3, 'Giant', 'mountain', 550, 'rented')
""")

connection.commit()
connection.close()

print("База данных создана")