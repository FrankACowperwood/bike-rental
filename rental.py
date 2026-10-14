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


def get_bicycles():
    connection = sqlite3.connect("bike_rental.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM bicycles")
    bicycles = cursor.fetchall()

    connection.close()

    result = []

    for bicycle in bicycles:
        result.append({
            "id": bicycle[0],
            "brand": bicycle[1],
            "type": bicycle[2],
            "price": bicycle[3],
            "status": bicycle[4]
        })

    return result


def rent_bicycle(bicycle_id, user_id):
    connection = sqlite3.connect("bike_rental.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM bicycles WHERE id = ?",
        (bicycle_id,)
    )

    bicycle = cursor.fetchone()

    if bicycle is None:
        connection.close()
        return "not_found"

    if bicycle[4] != "available":
        connection.close()
        return "unavailable"

    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        connection.close()
        return "user_not_found"

    cursor.execute(
        "UPDATE bicycles SET status = 'rented' WHERE id = ?",
        (bicycle_id,)
    )

    cursor.execute(
        """
        INSERT INTO rentals (bicycle_id, user_id, rented_at)
        VALUES (?, ?, datetime('now'))
        """,
        (bicycle_id, user_id)
    )

    connection.commit()
    connection.close()

    return "success"


def return_bicycle(bicycle_id):
    connection = sqlite3.connect("bike_rental.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM bicycles WHERE id = ?",
        (bicycle_id,)
    )

    bicycle = cursor.fetchone()

    if bicycle is None:
        connection.close()
        return "not_found"

    if bicycle[4] != "rented":
        connection.close()
        return "not_rented"

    cursor.execute(
        "UPDATE bicycles SET status = 'available' WHERE id = ?",
        (bicycle_id,)
    )

    cursor.execute(
        """
        UPDATE rentals
        SET returned_at = datetime('now')
        WHERE bicycle_id = ?
        AND returned_at IS NULL
        """,
        (bicycle_id,)
    )

    connection.commit()
    connection.close()

    return "success"
def get_rentals():
    connection = sqlite3.connect("bike_rental.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            rentals.id,
            bicycles.brand,
            users.name,
            rentals.rented_at,
            rentals.returned_at
        FROM rentals
        JOIN bicycles
            ON rentals.bicycle_id = bicycles.id
        LEFT JOIN users
            ON rentals.user_id = users.id
        ORDER BY rentals.id DESC
    """)

    rentals = cursor.fetchall()

    connection.close()

    result = []

    for rental in rentals:
        result.append({
            "id": rental[0],
            "bicycle": rental[1],
            "user": rental[2],
            "rented_at": rental[3],
            "returned_at": rental[4]
        })

    return result

    rentals = cursor.fetchall()

    connection.close()

    result = []

    for rental in rentals:
        result.append({
            "id": rental[0],
            "bicycle": rental[1],
            "rented_at": rental[2],
            "returned_at": rental[3]
        })

    return result

def get_users():
    connection = sqlite3.connect("bike_rental.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    connection.close()

    result = []

    for user in users:
        result.append({
            "id": user[0],
            "name": user[1],
            "email": user[2]
        })

    return result