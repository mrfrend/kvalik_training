import pymysql
# from dto.role import Role

connection = pymysql.connect(
    host="localhost", user="root", password="", database="kvalik"
)


def login(login: str, password: str):
    with connection.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        cur.execute(
            "SELECT * FROM accounts WHERE login = %s AND password = %s",
            (login, password),
        )
        result = cur.fetchone()
        return result


def get_reservations():
    with connection.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        query = """
            SELECT reservation.id, rooms.number, categories.category_name, room_status.status_name,
            CONCAT_WS(' ', clients.first_name, clients.last_name, clients.middle_name) as fio,
            check_in, check_out
            FROM reservation INNER JOIN
            rooms ON room_id = rooms.id
            INNER JOIN categories ON
            rooms.category_id = categories.id
            INNER JOIN room_status
            ON rooms.status_id = room_status.id
            INNER JOIN clients ON
            reservation.client_id = clients.id
        """
        cur.execute(query)
        result = cur.fetchall()
        return result

def get_clients_info():
    with connection.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        cur.execute("SELECT first_name, last_name, middle_name, passport_series, passport_number, cause_visit FROM clients")
        clients = cur.fetchall()
        return clients

def get_categories():
    with connection.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        cur.execute("SELECT id, category_name FROM categories")
        categories = cur.fetchall()
        return categories

def get_fio_clients():
    with connection.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        cur.execute("SELECT id, CONCAT_WS(' ', first_name, last_name, middle_name) as fio FROM clients")
        fios = cur.fetchall()
        return fios

def get_room_statuses():
    with connection.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        cur.execute("SELECT id, status_name FROM room_status")
        statuses = cur.fetchall()
        return statuses

def get_room_numbers():
    with connection.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        cur.execute("SELECT id, number from rooms")
        numbers = cur.fetchall()
        return numbers

def update_reservation(reservation_id: int, room_id: int, client_id: int, check_in: str, check_out: str):
    with connection.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        cur.execute("""
            UPDATE reservation
            SET room_id = %s, client_id = %s, check_in = %s, check_out = %s
            WHERE id = %s
        """, (room_id, client_id, check_in, check_out, reservation_id))
        connection.commit()

def add_new_client(first_name: str, last_name: str, middle_name: str, passport_series: int, passport_number: int, cause_visit: str):
    with connection.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        cur.execute("""INSERT INTO clients 
                    (first_name, last_name, middle_name, passport_series, passport_number, cause_visit)
                    VALUES (%s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, middle_name, passport_series, passport_number, cause_visit))
        connection.commit()

def get_available_rooms(check_in_date: str, check_out_date: str):
    with connection.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        query = """
            SELECT floor, number, categories.category_name
            FROM rooms
            INNER JOIN categories ON rooms.category_id = categories.id
            WHERE NOT EXISTS (
                SELECT 1 FROM reservation
                WHERE room_id = rooms.id
                AND check_in < %s AND check_out > %s
            )
        """
        cur.execute(query, (check_out_date, check_in_date))
        return cur.fetchall()
