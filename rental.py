import sqlite3

def show_available_bicycles():
    connection = sqlite3.connect("bike_rental.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM bicycles WHERE status = 'available'"
    )

    bicycles = cursor.fetchall()

    for bicycle in bicycles:
        print(
            bicycle[0],
            bicycle[1],
            bicycle[2],
            bicycle[3]
        )

    connection.close()

def rent_bicycle(bicycle_id):
    connection = sqlite3.connect("bike_rental.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM bicycles WHERE id = ?",
        (bicycle_id,)
    )

    bicycle = cursor.fetchone()

    if bicycle == None:
        print("Велосипеда нет")

    elif bicycle[4] == "available":
        cursor.execute(
            "UPDATE bicycles SET status = 'rented' WHERE id = ?",
            (bicycle_id,)
        )

        connection.commit()
        print("Велосипед успешно арендован")

    else:
        print("Велосипед недоступен")

    connection.close()