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
INSERT OR IGNORE INTO bicycles (id, brand, type, price, status)
VALUES (1, 'Trek', 'mountain', 500, 'available')
""")

cursor.execute("""
INSERT OR IGNORE INTO bicycles (id, brand, type, price, status)
VALUES (2, 'Cube', 'road', 400, 'available')
""")

cursor.execute("""
INSERT OR IGNORE INTO bicycles (id, brand, type, price, status)
VALUES (3, 'Giant', 'mountain', 550, 'rented')
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS rentals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bicycle_id INTEGER NOT NULL,
    rented_at TEXT NOT NULL,
    returned_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")

cursor.execute("""
INSERT OR IGNORE INTO users (id, name, email)
VALUES (1, 'Андрей', 'andrey@example.com')
""")

cursor.execute("""
INSERT OR IGNORE INTO users (id, name, email)
VALUES (2, 'Екатерина', 'ekaterina@example.com')
""")

try:
    cursor.execute("""
    ALTER TABLE rentals
    ADD COLUMN user_id INTEGER
    """)
except sqlite3.OperationalError:
    pass

connection.commit()
connection.close()

print("База данных создана")

