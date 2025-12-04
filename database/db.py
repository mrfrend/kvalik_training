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
            SELECT rooms.number, categories.category_name, room_status.status_name,
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
